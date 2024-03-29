# demand forecasting model
import os
from flask import Flask, jsonify
from dotenv import load_dotenv
import requests
import json
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)
load_dotenv()

"""
Expected format in DemandForecast database:
--------------------------------------------------------
| Date       | expectedCustomers | peakHours | weather |
--------------------------------------------------------
| 2024-01-01 | 300               | 12-2      | rain    |
| 2024-01-02 | 900               | 12-2      | sunny   |
| 2024-01-03 | 300               | 12-2      | sunny   |
| 2024-01-04 | 300               | 12-2      | rain    |
| 2024-01-05 | 500               | 12-2      | sunny   |
| 2024-01-06 | 600               | 12-2      | sunny   |
| 2024-01-07 | 700               | 12-2      | sunny   |
"""

# Hardcoded demand data
expected_customers_per_day = {
    "Monday": 300,
    "Tuesday": 900,
    "Wednesday": 300,
    "Thursday": 300,
    "Friday": 500,
    "Saturday": 700,
    "Sunday": 700,
}

# Hardcoded 2024 Public Holidays data: taken from https://www.mom.gov.sg/employment-practices/public-holidays
public_holidays = {
    "2024-01-01": "New Year's Day",
    "2024-02-10": "Chinese New Year",
    "2024-02-11": "Chinese New Year",
    "2024-03-29": "Good Friday",
    "2024-04-10": "Hari Raya Puasa",
    "2024-05-01": "Labour Day",
    "2024-05-22": "Vesak Day",
    "2024-07-17": "Hari Raya Haji",
    "2024-08-09": "National Day",
    "2024-10-31": "Deepavali",
    "2024-12-25": "Christmas Day",
}


# Endpoint to fetch weather forecast
@app.route("/weather_forecast", methods=["GET"])
def get_weather_forecast():
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    lat = 1.251675284654383  # lat and lon of good old days
    lon = 103.81719661065192
    # today_date = datetime.now().strftime("%Y-%m-%d")
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


# Endpoint to get demand forecast
@app.route("/demand_forecast", methods=["GET"])
def get_demand_forecast():
    """
    1. Date: get today's date
    2. Expected Customers
          2.1. Check if today is a public holiday, if today is a PH, take Sat demand number as baseline
          2.2. Get weather data:
                  if rain chance >50% at 9am, demand *0.95:
                  if rain chance <50% at 9am AND rain chance > 50% ANY TIME after 12pm, demand *1.03
                  else demand same
    3. Weather:
          if rain_chance[9am, 12noon, 3pm, 6pm] > 50% : rainy
          else: sunny
    4. Store data in sql
    """
    current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date
    current_day = datetime.now().strftime("%A")  # Get the current day of the week

    # get today's date + next 4 days (e.g. [(2024-03-29, Thursday), (2024-03-30, Friday), (2024-03-31, Saturday), (2024-04-01, Sunday), (2024-04-02, Monday)] )
    five_day_prediction = [(current_date, current_day)]
    for i in range(1, 5):
        five_day_prediction.append(
            (
                (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
                (datetime.now() + timedelta(days=i)).strftime("%A"),
            )
        )

    # get weather data
    weather_data = get_weather_forecast()
    forecast_demand = []
    for curr_date, curr_day in five_day_prediction:
        # check if today is a public holiday
        if curr_day in public_holidays:
            expected_customers = expected_customers_per_day.get("Saturday")
        else:
            expected_customers = expected_customers_per_day.get(curr_day)

        # get rain chance data
        rain_3h = weather_data.get(curr_date)
        weather_status = "sunny"
        for time, rain_chance in rain_3h:
            # Rain before 9am
            if time == "09:00:00" and rain_chance > 0.5:
                expected_customers = expected_customers * 0.95  # 0.95 hardcoded
                weather_status = "rainy"
            # No rain before 9am and rain after 12pm
            elif time != "09:00:00" and rain_chance > 0.5:
                expected_customers = expected_customers * 1.03  # 1.03 hardcoded
                weather_status = "rainy"
            expected_customers = round(expected_customers)
        forecast_demand.append([curr_date, expected_customers, weather_status])
    return jsonify(forecast_demand)


# @app.route("/store_demand_forecast", methods=["POST"])
# def store_demand_forecast():
#     conn = sqlite3.connect("DemandForecast.db")
#     c = conn.cursor()
#     c.execute(
#         """CREATE TABLE IF NOT EXISTS DemandForecast (Date TEXT, expectedCustomers INTEGER, peakHours TEXT, weather TEXT)"""
#     )
#     forecast_demand = get_demand_forecast()
#     for date, expected_customers, weather in forecast_demand:
#         c.execute(
#             f"INSERT INTO DemandForecast VALUES ('{date}', {expected_customers}, '12-2', '{weather}')"
#         )
#     conn.commit()
#     conn.close()
#     return jsonify({"message": "Data stored successfully"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
