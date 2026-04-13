import os
from dotenv import load_dotenv
import requests
import datetime

load_dotenv()

# Urls and tokens
BASE_URL = os.getenv("NUTRITION_API_BASE_URL")
X_APP_ID = os.getenv("NUTRITION_API_X_APP_ID")
X_APP_KEY = os.getenv("NUTRITION_API_X_APP_KEY")
SHEETY_URL = os.getenv("SHEETY_URL")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

# User details
GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 185
AGE = 23


today = datetime.date.today().strftime("%d/%m/%Y")
now = datetime.datetime.now().strftime("%H:%M:%S")

user_exercise = input("Tell me which exercise you did: ").title()


# 1.Nutritionix Parsing
exercise_data = {
    "query": user_exercise,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY,
}

nutritionix_response = requests.post(
    url=f"{BASE_URL}/v1/nutrition/natural/exercise",
    headers=headers,
    json=exercise_data
)
exercises = nutritionix_response.json()["exercises"]

# 2.Save a row to Sheety
for exercise in exercises:
    workouts = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": SHEETY_BEARER_TOKEN,
    }

    sheety_response = requests.post(url=SHEETY_URL, json=workouts,headers=bearer_headers)
    print(sheety_response.status_code)
    print(sheety_response.json())