import requests
import os
import json
from tests.utils.env_valueGet import env_value_get

BASE_URL, TOKEN, ID = env_value_get()

def test_get_next_instruction():
    """ 获取下一步指引 """
    url = f"{BASE_URL}/v1/instructions/next"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Next Instruction:", data["instruction"])
    else:
        print(f"Failed to fetch next instruction: {response.status_code}, {response.text}")

if __name__ == '__main__':
    test_get_next_instruction()
