import requests
from aiogram import Bot, Dispatcher, types, executor


API_TOKEN = '7339194371:AAHmWO1GKH5kLwRweTdxI0dlKj-U8vJgqw8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
async def set_commands(bot: Bot):
  commands = [
    types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
    types.BotCommand(command='/get_consult', description='Консультант'),
    types.BotCommand(command='/get_picture', description='Здарова!'),
  ]

  await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я нейроконсультант, задай мне интересный вопрос, отвечу по сути!')
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
        "text": "сторого отвечай да или нет на вопросы пользователя"
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