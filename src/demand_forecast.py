# demand forecasting model
import json
from flask import jsonify
import requests
from datetime import datetime, timedelta
from db_utils import execute_query
from darts import TimeSeries
from darts.models import ARIMA
import pandas as pd

"""
DemandForecast table:
--------------------------------------------------------
| Date       | Day     | Time     | expectedCustomers  | 
--------------------------------------------------------
| 2024-01-01 | Monday  | 10:00:00 | 9                  |
| 2024-01-01 | Monday  | 11:00:00 | 23                 |
| 2024-01-01 | Monday  | 12:00:00 | 42                 |
| 2024-01-01 | Monday  | 13:00:00 | 50                 |
| 2024-01-01 | Monday  | 14:00:00 | 46                 |
| 2024-01-01 | Monday  | 15:00:00 | 34                 |
| 2024-01-01 | Monday  | 16:00:00 | 26                 |
| 2024-01-01 | Monday  | 17:00:00 | 23                 |
| 2024-01-01 | Monday  | 18:00:00 | 23                 |
| 2024-01-01 | Monday  | 19:00:00 | 24                 |
| 2024-01-01 | Monday  | 20:00:00 | 19                 |
| 2024-01-01 | Monday  | 21:00:00 | 12                 |
| 2024-01-01 | Tuesday | 10:00:00 | 42                 |
| 2024-01-01 | Tuesday | 11:00:00 | 79                 |
| 2024-01-01 | Tuesday | 12:00:00 | 100                |
| 2024-01-01 | Tuesday | 13:00:00 | 99                 |
| 2024-01-01 | Tuesday | 14:00:00 | 77                 |
| 2024-01-01 | Tuesday | 15:00:00 | 45                 |
| 2024-01-01 | Tuesday | 16:00:00 | 30                 |
"""
"""
Flow:
PastDemand -> time series prediction model -> Alter with Weather data -> DemandForecast
"""

# Loading expected customers and public holidays data
with open("../data/json/expected_customers.json") as f:
    expected_customers = json.load(f)
with open("../data/json/public_holidays.json") as f:
    public_holidays = json.load(f)


# get today's date + next 6 days (e.g. [(2024-03-29, Thursday), (2024-03-30, Friday), (2024-03-31, Saturday), (2024-04-01, Sunday), (2024-04-02, Monday), (2024-04-03, Tuesday), (2024-04-04, Wednesday)] )
def list_of_next_seven_days():
    current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date
    current_day = datetime.now().strftime("%A")  # Get the current day of the week
    seven_day_prediction = [(current_date, current_day)]
    for i in range(1, 7):
        seven_day_prediction.append(
            (
                (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
                (datetime.now() + timedelta(days=i)).strftime("%A"),
            )
        )
    return seven_day_prediction

# Fetch PastDemand data
def get_past_demand():
    query = "SELECT * FROM PastDemand"
    result = execute_query(query)
    past_demand_data = [{'Date': str(row[0]), 'Day': row[1], 'Time': str(row[2]), "Customers": row[3]} for row in result]
    df = pd.DataFrame(past_demand_data)
    return df

# # For testing locally
# def get_past_demand():
#     df = pd.read_csv("../data/csv/04-mock_customer_demand_past.csv", index_col=False)
#     return df

# Fit PastDemand data into model and predict next week's demand
# # I'll be using Darts library for time series forecasting: Documentation: https://unit8co.github.io/darts/
def arima_next_week_demand():
    today_date = str(list_of_next_seven_days()[0][0])
    past_demand_df = get_past_demand()  # Get past demand data
    past_demand_df = past_demand_df[
        past_demand_df["Date"] < today_date
    ]  # I only want to fit in the data that is before today

    # Wrangle data into TimeSeries format
    past_demand_df["DateTime"] = pd.to_datetime(
        past_demand_df["Date"] + " " + past_demand_df["Time"]
    )
    past_demand_df = past_demand_df.drop(columns=["Date", "Time"])
    # Convert to TimeSeries object. Because the data is only from 10am to 9pm, need to fill the missing time slots with 0.
    past_demand_time_series = TimeSeries.from_dataframe(
        past_demand_df,
        time_col="DateTime",
        value_cols="Customers",
        fill_missing_dates=True,
        freq="h",
        fillna_value=0,
    )

    # ARIMA model
    model = ARIMA(p=24)
    model.fit(past_demand_time_series)
    prediction = model.predict(168)

    # Wrangle prediction data into the format of DemandForecast table
    prediction_df = TimeSeries.pd_dataframe(prediction)
    prediction_df["DateTime"] = prediction_df.index
    prediction_df["Date"] = prediction_df["DateTime"].dt.strftime("%Y-%m-%d")
    prediction_df["Time"] = prediction_df["DateTime"].dt.strftime("%H:%M:%S")
    prediction_df["Day"] = prediction_df["DateTime"].dt.strftime("%A")
    prediction_df["ExpectedCustomers"] = prediction_df["Customers"].astype(int)
    opening_hours = [
        "10:00:00",
        "11:00:00",
        "12:00:00",
        "13:00:00",
        "14:00:00",
        "15:00:00",
        "16:00:00",
        "17:00:00",
        "18:00:00",
        "19:00:00",
        "20:00:00",
        "21:00:00",
    ]
    prediction_df = prediction_df[prediction_df["Time"].isin(opening_hours)]
    result_df = prediction_df[["Date", "Day", "Time", "ExpectedCustomers"]]
    result_df = result_df.reset_index(drop=True)
    return result_df

# Get's the rain chance of current day and the next 4 days
def weather_forecast():
    api_key = (
        "745e49dcd551b66c18a13052f7852b0a"  # Move to .env in future implementations
    )
    lat = 1.251675284654383  # lat and lon of good old days
    lon = 103.81719661065192
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        daily_rain_chance = (
            dict()
        )  # List to store {date: [rain_chance_9am, rain_chance_12noon, rain_chance_3pm, rain_chance_6pm]}

        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]
            time = item["dt_txt"].split(" ")[1]
            time_in_opening_hours = ["09:00:00", "12:00:00", "15:00:00", "18:00:00"]
            if time not in time_in_opening_hours:
                continue
            if date not in daily_rain_chance:
                daily_rain_chance[date] = []
            daily_rain_chance[date].append((time, item["pop"]))
        return daily_rain_chance
    else:
        return jsonify({"error": "Failed to fetch weather forecast"}), 500

# Generates demand forecast for the next 7 days, however, only the demand of the first five days will be influenced by the weather data
def seven_days_demand_forecast():
    """
    1. Date, Day: Get today's date and day
    2. Expected Customers
          2.1. Check if today is a public holiday, if today is a PH, take Sat demand number as baseline
          2.2. Get weather data:
                  if rain chance >50% at 9am, demand *0.7:
                  if rain chance <50% at 9am AND rain chance > 50% ANY TIME after 12pm, demand *1.10
                  else demand same
    3. Return data in the format of [Date, Day, Time, expectedCustomers]
    """
    df = arima_next_week_demand()
    weather_data = weather_forecast()
    for rain_date, rain_3h in weather_data.items():
        for time, rain_chance in rain_3h:
            if time == "09:00:00" and rain_chance > 0.5:
                # 10 am and 11 am demand data * 0.7
                df.loc[(df['Date'] == rain_date) & (df['Time'].isin(["10:00:00", "11:00:00"])), 'ExpectedCustomers'] *= 0.7
            elif time != "09:00:00" and rain_chance > 0.5:
                # 12 - 9 pm demand * 1.10
                df.loc[(df['Date'] == rain_date) & (df['Time'].isin([f"{hour}:00:00" for hour in range(12, 22)])), 'ExpectedCustomers'] *= 1.1
    df['ExpectedCustomers'] = df['ExpectedCustomers'].astype(int)
    return df
