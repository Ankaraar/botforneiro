import requests
import base64
import time
from random import randint
from aiogram import Dispatcher, Bot, types, executor

API_KEY = '7314860258:AAFaBfKUREQPj1p2Mf43wtuCYSLPkwP99xI'

bot = Bot(token= API_KEY)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я твой Шедеврум!')


def generate_image(prompt_text):

    prompt = {
        "modelUri": "art://b1g3f13cj7d6d3ss2md9/yandex-art/latest",
        "generationOptions": {
          "seed": randint(10000, 200000000000000)
        },
        "messages": [
          {
            "weight": 1,
            "text": prompt_text
          }
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwb7GzleJZRaOKtwO-wuyg_7o1-oKs1gr1Wgn"
    }
    response = requests.post(url=url, headers=headers, json=prompt)
    result = response.json()
    operation_id = result['id']

    operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"

    while True:
        operation_response = requests.get(operation_url, headers=headers)
        operation_result = operation_response.json()
        if 'response' in operation_result:
            image_base64 = operation_result['response']['image']
            image_data = base64.b64decode(image_base64)
            return image_data
        else:
            time.sleep(5)