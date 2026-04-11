
from twilio.rest import Client
import requests

# Twilio SMS
account_sid = 'AC7b1158327769801bb9a509023db7115d'
auth_token = 'ecdf139336abd8aae59e254ce42cb8ed'

# Open whether map
api_key= "d462c4e6840a2efdea635324dad6dda2"
# Check if rains
# Bring an umbrella if status code < 700
weather_params ={
    "lat" : 42.6977,
    "lon" : 23.3219,
    "appid": api_key,
    "cnt": 4,
}

response= requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast",params=weather_params)
response.raise_for_status()

data = response.json()

will_rain = False

for weather in data["list"]:
    weather_id = weather["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("Rain SMS sent!")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+359884847216",
        from_="+15754002212",
        body=f"Rain is coming! Do not forget to get an umbrella!",)


print(message.status)