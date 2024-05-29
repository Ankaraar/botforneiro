from aiogram import Bot, Dispatcher, types, executor
from magic import get_response
from shedewr import generate_image
from consult import get_consult


api_key = '6767940798:AAGA8rRP9qoY_gRmlqLAfX0UvInHM8adKJI'

bot = Bot(token= api_key)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/get_consult', description='Консультант'),
        types.BotCommand(command='/get_picture', description='Здарова!'),

    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я твой первый бот!')

@dp.message_handler(commands='get_consult')
async def consult(message: types.Message):
    text = message.get_args()
    print(text)
    response_consult = await get_response(message.text)
    await message.answer(response_consult)

@dp.message_handler(commands='get_picture')
async def consult(message: types.Message):
    text = message.get_args()
    response_text = await get_response(text)
    await message.reply(f'Вот твой волшебный промпт: {response_text}')
    await message.reply('Готовится')
    try:
        image_data = generate_image(response_text)
        await message.reply_photo(photo= image_data)
    except Exception as е:
        await message.reply(f'Произошла ошибка {е}')


@dp.message_handler(commands='get_consult')
async def get_consult(message: types.Message):
    await message.reply('Приветствую!')

@dp.message_handler(commands='get_picture')
async def get_picture(message: types.Message):
    await message.reply('Здарова')


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)