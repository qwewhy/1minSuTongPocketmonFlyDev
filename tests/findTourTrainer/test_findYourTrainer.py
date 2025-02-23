import requests
import os
import json
from tests.utils.env_valueGet import env_value_get

BASE_URL, TOKEN, ID = env_value_get()

def test_get_me_trainer_name():
    url = f"{BASE_URL}/v1/trainers"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)

    print("My ID from TRAINER_DATA.json:", ID)
    print("My Token from TRAINER_DATA.json:", TOKEN)
    url = f"{BASE_URL}/v1/trainers"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
        if "data" in data:
            trainers = data["data"]
            my_trainer = next((t for t in trainers if t["_id"] == ID), None)
            print(" \n === All Trainers ==")
            for trainer in trainers:
                print(f" - ID: {trainer['_id']}, Name: {trainer['name']}")

            if my_trainer:
                print("My Trainer Name:", my_trainer["name"])
            else:
                print("Trainer not found")
        else:
            print("No trainers found")

    except Exception as e:
        print(f"Failed to fetch trainer name: {response.status_code}, {response.text}")

def get_my_trainer_info():
    url = f"{BASE_URL}/v1/trainers/me"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.get(url, headers=headers)
    data = response.json()
    print("My Trainer Info:", json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    test_get_me_trainer_name()
    #get_my_trainer_info()
