import requests
import json

url="https://prodapi.metweb.ie/observations/bray/today"
response = requests.get(url)
data = response.json()
print(data)
for row in data:
  ##"dayName":"Sunday","date":"01-12-2019","reportTime":"00:00"
  print(row["dayName"],row["date"],row["reportTime"],row["temperature"])