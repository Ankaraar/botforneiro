import requests
from aiogram import Bot, Dispatcher, types, executor


API_TOKEN = '7438907175:AAEYp948Jer317UXb2dpFNQalSbmGeNly_E'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я нейроконсультант, могу помочь тебе с решением примеров!')
async def get_response(message_text):
  prompt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
      "stream": False,
      "temperature": 0,
      "maxTokens": "2000"
    },
    "messages": [
      {
        "role": "system",
        "text": "ты - программа для расчета примеров, решай примеры по запросу пользователя и выводи в ввиде чисел "
      },
      {
        "role": "user",
        "text": message_text
      }
    ]
  }
  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key AQVN2JvfAWyMdNLf1b04PcAkGoRikWJgT2o2mcq1"
  }
  response = requests.post(url, headers=headers, json=prompt)
  result = response.json()
  print(result)
  return result['result']['alternatives'][0]['message']['text']
@dp.message_handler()
async def analize_message(message:types.Message):
  response_text = await get_response((message.text))
  await message.answer(response_text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)