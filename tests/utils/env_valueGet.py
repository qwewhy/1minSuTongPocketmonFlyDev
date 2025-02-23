import os
import json

def env_value_get():
    # 获取当前文件所在目录的上一级目录，解析BASE_URL.json的路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(BASE_DIR, 'env', 'BASE_URL.json')

    with open(config_path, "r") as f:
        config = json.load(f)

    BASE_URL = config.get("BASE_URL", "https://pocketmon.fly.dev/")

    trainer_data_path = os.path.join(BASE_DIR, 'env', 'TRAINER_DATA.json')
    with open(trainer_data_path, "r") as f:
        trainer_data = json.load(f)

    TOKEN = trainer_data.get("token", "token")
    ID = trainer_data.get("_id", "_id")

    return BASE_URL, TOKEN, ID