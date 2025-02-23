import requests
import pytest
import os
import json
from tests.utils.env_valueGet import env_value_get

BASE_URL, TOKEN, ID = env_value_get()

def test_create_trainer_false():
    url = f"{BASE_URL}/v1/trainers"
    payload = {
        "name": "扣1给服务器上上强度",
        "password": "password123",
        "gender": "male123",
        "language": "chinese"
    }
    response = requests.post(url, json=payload)
    # 根据API文档检查正确的状态码，如200或201
    assert response.status_code in [200, 201], f"Unexpected status: {response.status_code}"
    data = response.json()
    trainer_data = data["data"]
    # 检查返回数据中是否包含预期字段
    assert "token" in trainer_data, "Token not found in response"
    assert "_id" in trainer_data, "ID not found in response"


@pytest.mark.parametrize("payload, expected_status", [
    ({"name": "", "password": "123456"}, 400),  # 示例：空名称导致错误
    ({"name": "Misty", "password": "123"}, 400),  # 示例：密码过短
    ({"name": "Misty", "password": "123456", "gender": "Armed helicopter", "language": "chinese"}, 400),  # 示例：性别错误
])
def test_create_trainer_fail(payload, expected_status):
    url = f"{BASE_URL}/v1/trainers"
    response = requests.post(url, json=payload)
    assert response.status_code == expected_status, f"Expected {expected_status} but got {response.status_code}"
