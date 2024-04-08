import csv
from datetime import date, timedelta, time
import random 

# number of days to go back (6 months = 180 days)
days_back = 180

# target demand (mean) for customer, obtained from google popular times
data = {
  '1000': [9, 42, 19, 11, 15, 9, 14],
  '1100': [23, 79, 31, 22, 32, 22, 34],
  '1200': [42, 100, 44, 38, 49, 3, 49],
  '1300': [50, 99, 47, 48, 50, 46, 57],
  '1400': [46, 77, 38, 38, 43, 49, 54],
  '1500': [34, 45, 35, 29, 36, 40, 47],
  '1600': [26, 30, 33, 25, 34, 36, 42],
  '1700': [23, 25, 29, 26, 35, 42, 44],
  '1800': [23, 28, 26, 29, 37, 50, 45],
  '1900': [24, 20, 20, 24, 36, 47, 38],
  '2000': [19, 14, 15, 20, 27, 31, 24],
  '2100': [12, 7, 7, 10, 18, 13, 12]
}

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hrs = ['1000', '1100', '1200', '1300', '1400', '1500', '1600', '1700', '1800', '1900', '2000', '2100']
day_idx_mapping = {day: idx for idx, day in enumerate(days)}

# Define starting date (31st jan - 6 months)

may_10th_2024 = date(year=2024, month=5, day=10)
start_date = may_10th_2024

with open('mock_customer_demand_past.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['Date', 'Day', 'Time', 'Customers'])  # Write header row

  for day in range(days_back):
    current_date = start_date - timedelta(days=day)
    # print(current_date)
    date_str = current_date.strftime("%Y-%m-%d")
    day_of_week = current_date.strftime("%A")

    for hr in hrs:
        # print(hr)
        hr_time = time(hour=int(hr[:2]), minute=0, second=0)
        time_str = hr_time.strftime("%H:%M:%S")
        idx = day_idx_mapping[day_of_week]
        mu = data[hr][idx]  # original data (like mean value)
        sigma = mu * 0.05  # Standard deviation (5% of original data)
        new_value = round(random.gauss(mu, sigma))  # Use random.gauss for small deviation
        # Ensure non-negative customer flow
        new_value = max(0, new_value)
        new_row = [date_str, day_of_week, time_str, new_value]
        writer.writerow(new_row)

print("Customer flow data for the past 6 months generated and saved to customer_demand_past.csv")
