from aiogram import Dispatcher, Bot, types, executor
from neiro.neiro_gen import get_image
from neiro_assistent import get_response


API = '7183212022:AAG99IqBJFxRmHnwyFcb-g1hFzZxt390Fws'

bot = Bot(token= API)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Попробуй мою нейронку!')


# @dp.message_handler()
# async def analize_message(message:types.Message):
#   response_text = await get_response((message.text))
#   await message.answer(response_text)


@dp.message_handler()
async def handle_message(message:types.Message):
    response_text = await get_response(message.text)
    user_text = response_text
    print(user_text)
    await message.reply('генерация изображения!')

    try:
        image_data = get_image(user_text)
        print(image_data)
        await message.reply_photo(photo=image_data)
    except Exception as е:
        await message.reply(f'Произошла ошибка {е}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
