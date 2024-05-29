import requests

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
        "text": "Ты — нейронная сеть, которая может улучшить запрос от пользователя, он передает тебе запрос, ты его улучшаешь в единичном формате и передаешь в нейронную сеть для генерации картинки "
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

# @dp.message_handler()
# async def analize_message(message:types.Message):
#   response_text = await get_response((message.text))
#   await message.answer(response_text)
