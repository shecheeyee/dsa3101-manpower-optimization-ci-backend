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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
