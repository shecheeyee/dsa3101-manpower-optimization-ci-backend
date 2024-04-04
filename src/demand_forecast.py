# demand forecasting model
import os
import json
from flask import jsonify
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta

load_dotenv()

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

# Loading expected customers and public holidays data, if these 2 files are in the same directory as this file
with open("expected_customers.json") as f:
    expected_customers = json.load(f)
with open("public_holidays.json") as f:
    public_holidays = json.load(f)


# Get's the rain chance of current day and the next 4 days
def weather_forecast():
    api_key = "745e49dcd551b66c18a13052f7852b0a"
    lat = 1.251675284654383  # lat and lon of good old days
    lon = 103.81719661065192
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        daily_rain_chance = (dict())  # List to store {date: [rain_chance_9am, rain_chance_12noon, rain_chance_3pm, rain_chance_6pm]}

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
def demand_forecast():
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
    current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date
    current_day = datetime.now().strftime("%A")  # Get the current day of the week

    # get today's date + next 6 days (e.g. [(2024-03-29, Thursday), (2024-03-30, Friday), (2024-03-31, Saturday), (2024-04-01, Sunday), (2024-04-02, Monday), (2024-04-03, Tuesday), (2024-04-04, Wednesday)] )
    seven_day_prediction = [(current_date, current_day)]
    for i in range(1, 7):
        seven_day_prediction.append(
            (
                (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
                (datetime.now() + timedelta(days=i)).strftime("%A"),
            )
        )

    # Get weather data
    weather_data = weather_forecast()
    forecast_demand = []
    for curr_date, curr_day in seven_day_prediction:
        # check if today is a public holiday
        hourly_demand = []
        day_index = None

        # if today is a public holiday, take Sat demand number as baseline
        if curr_date in public_holidays.keys():
            day_index = 5  # 5 is saturday demand
        else:
            day_index = datetime.strptime(curr_date, "%Y-%m-%d").weekday()
        # store daily demand data dict(time: customers)
        for _, customers in expected_customers.items():
            hourly_demand.append(customers[day_index])

        # get rain chance data, and adjust demand accordingly
        if (curr_date in weather_data.keys()):  # This is for the first 5 dates (i.e. those that are in weather data)
            rain_3h = weather_data.get(curr_date)
            for time, rain_chance in rain_3h:
                # If Rain before 9am, the 10 and 11 am demand data * 0.7
                if time == "09:00:00" and rain_chance > 0.5:
                    for i in range(2):
                        hourly_demand[i] = round(hourly_demand[i] * 0.7)  # 0.7 hardcoded
                # elif (no rain before 9am) AND (rain after 12pm), the 12 - 9 pm demand * 1.10
                elif time != "09:00:00" and rain_chance > 0.5:
                    for i in range(2, 12):
                        hourly_demand[i] = round(hourly_demand[i] * 1.10)  # 1.10 hardcoded

        # Append to forecast_demand
        for i, hourly_customers in enumerate(hourly_demand):
            forecast_demand.append(
                [curr_date, curr_day, f"{i+10}:00:00", hourly_customers]
            )
    return forecast_demand
