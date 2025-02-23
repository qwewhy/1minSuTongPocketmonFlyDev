from os import write
import requests
import pytest
import os
import json

from tests.utils.env_valueGet import env_value_get

# 获取当前文件所在目录的上一级目录，解析BASE_URL.json的路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(BASE_DIR, 'env', 'BASE_URL.json')

with open(config_path, "r") as f:
    config = json.load(f)

BASE_URL = config.get("BASE_URL", "https://pocketmon.fly.dev/")

# 用于存储成功返回的训练师的 token 和 _id
TRAINER_DATA = {}

def test_create_trainer_success():
    """ 成功创建训练师 """
    url = f"{BASE_URL}/v1/trainers"
    payload = {
        "name": "Hongyuan",
        "password": "password123",
        "gender": "male",
        "language": "english"
    }
    response = requests.post(url, json=payload)

    # 确保 API 返回正确的状态码
    assert response.status_code in [200, 201], f"Unexpected status: {response.status_code}"

    data = response.json()
    trainer_data = data["data"]

    # 确保返回的数据包含 token 和 _id
    assert "token" in trainer_data, "Token not found in response"
    assert "_id" in trainer_data, "ID not found in response"

    # 存储 token 和 _id 以便后续测试使用
    TRAINER_DATA["token"] = trainer_data["token"]
    TRAINER_DATA["_id"] = trainer_data["_id"]

    print("my token:",TRAINER_DATA["token"])
    print("my _id:",TRAINER_DATA["_id"])

    # 用于后续测试,训练师的信息存储在 env/TRAINER_DATA.json 文件中
    # 获取当前文件所在目录的上一级目录，解析BASE_DIR.json的路径
    trainer_data_path = os.path.join(BASE_DIR, 'env', 'TRAINER_DATA.json')
    with open(trainer_data_path, "w") as f:
        json.dump(TRAINER_DATA, f, indent=4)
    print(f"Trainer token and ID saved in {trainer_data_path}")
