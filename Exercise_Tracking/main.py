import os
import requests
from datetime import datetime
GENDER = "Female"
WEIGHT = 50
HEIGHT = 134
AGE = 20

API_ID = os.environ["NUTRITION_API_ID"]
API_KEY = os.environ["NUTRITION_API_KEY"]

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = os.environ["MY_SHEETY_ENDPOINT"]

headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY
}

exercise_text = input("Tell me which exercises you did: ")

params = {
    "query" : exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(
            os.environ["MY_USERNAME"],
            os.environ["MY_PASSWORD"],
        )
    )
