import requests

api_key= "d462c4e6840a2efdea635324dad6dda2"

weather_params ={
    "lat" : 42.6977,
    "lon" : 23.3219,
    "appid": api_key,
}

# Current time
print("Currrent weather:")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?",params=weather_params)
data = response.json()
response.raise_for_status()
print(response.status_code)

data = response.json()
print(data)

# 5-day forecast
#https://api.openweathermap.org/data/2.5/forecast?lat=42.6977&lon=23.3219&appid=d462c4e6840a2efdea635324dad6dda2
print("\n5 day forecast")
response1= requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast",params=weather_params)
response1.raise_for_status()
print(response1.status_code)
data = response1.json()
print(data)


# Accesss only timestamps in the near future
weather_params1 ={
    "lat" : 42.6977,
    "lon" : 23.3219,
    "appid": api_key,
    "cnt": 3,
}
print("\n5 day forecast")
response2= requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast",params=weather_params1)
response2.raise_for_status()
print(response2.status_code)
data = response2.json()
print(data)


