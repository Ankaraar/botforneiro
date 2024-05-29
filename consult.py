import requests
from aiogram import Bot, Dispatcher, types, executor
API_TOKEN = '7076058873:AAHHMksEX5f2ZUhQBnbki3V2Z0H126EoW3k'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def get_consult(message_text):

  prompt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
      "stream": False,
      "temperature": 1,
      "maxTokens": "2000"
    },
    "messages": [
      {
        "role": "system",
        "text": "Выводи наилучший вариант ответа, по запросу пользователя, не более одного предложения"
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
  consult = result['result']['alternatives'][0]['message']['text']
  return consult