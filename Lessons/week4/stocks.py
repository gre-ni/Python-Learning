from datetime import date, timedelta
import json
import requests
import sys


key = "2GWANRKYXQK5NK59"
symbol = input("Which stock: ")

# TODO: Fix the day to filter out Saturdays and Sundays when stock market is closed
today = date.today()
yesterday = today - timedelta(days=1)
day_before = today - timedelta(days=2)

# print(today)
# print(yesterday)

try:
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&interval=5min&apikey=" + key)
except requests.RequestException:
    sys.exit("Invalid request")

# print(json.dumps(response.json(), indent=2))

info = response.json()
close_price = info["Time Series (Daily)"][str(yesterday)]["4. close"]

print(f"$ {close_price}")