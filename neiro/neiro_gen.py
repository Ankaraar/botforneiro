import requests
import base64
import time
from random import randint
# from aiogram import Dispatcher, Bot, types, executor
#
# API = '7183212022:AAG99IqBJFxRmHnwyFcb-g1hFzZxt390Fws'
#
# bot = Bot(token= API)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer('Попробуй мою нейронку!')



def get_image(prompt_text):

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
    print(result)
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
            print('Идет генерация, ожидайте!')
            time.sleep(5)

# @dp.message_handler()
# async def handle_message(message:types.Message):
#     user_text = message.text
#     await message.reply('генерация изображения!')
#
#     try:
#         image_data = get_image(user_text)
#         await message.reply_photo(photo=image_data)
#     except Exception as е:
#         await message.reply(f'Произошла ошибка {е}')
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
