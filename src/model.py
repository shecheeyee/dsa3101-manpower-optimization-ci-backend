# demand forecasting model
import os
from flask import Flask, jsonify
from dotenv import load_dotenv
import requests
import json
from datetime import datetime


app = Flask(__name__)
load_dotenv()


# Endpoint to fetch weather forecast
@app.route("/weather_forecast", methods=["GET"])
def get_weather_forecast():
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    lat = 1.251675284654383 # lat and lon of good old days
    lon = 103.81719661065192
    # today_date = datetime.now().strftime("%Y-%m-%d")
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        daily_rain_chance = []  # List to store (date, time, rain_chance) tuples

        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]
            time = item["dt_txt"].split(" ")[1]
            rain_chance = item["pop"]
            daily_rain_chance.append((date, time, rain_chance))
        return jsonify(daily_rain_chance)
    else:
        return jsonify({"error": "Failed to fetch weather forecast"}), 500

# Hardcoded demand data
demand_data = {
    "Monday": 300,
    "Tuesday": 900,
    "Wednesday": 300,
    "Thursday": 300,
    "Friday": 500,
    "Saturday": 600,
    "Sunday": 700,
}

# Endpoint to get demand forecast
@app.route("/demand_forecast", methods=["GET"])
def get_demand_forecast():
    # Get the current day of the week
    current_day = datetime.now().strftime("%A")
    # Get the demand for today
    today_demand = demand_data.get(current_day)
    if today_demand is not None:
        return jsonify({current_day: today_demand}), 200
    else:
        return jsonify({"error": "Demand data not available for today"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
