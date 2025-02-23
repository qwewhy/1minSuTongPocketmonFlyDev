import requests
import os
import json
from tests.utils.env_valueGet import env_value_get

BASE_URL, TOKEN, ID = env_value_get()

def test_get_full_list_of_trainers():
    url = f"{BASE_URL}/v1/trainers"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("list of trainers", data["data"])
    else:
        print(f"Failed to fetch list of trainer: {response.status_code}, {response.text}")

if __name__ == '__main__':
    test_get_full_list_of_trainers()
