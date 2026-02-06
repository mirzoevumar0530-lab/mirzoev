from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio

API_TOKEN = "
"  # Инҷо токени боти Telegram-ро гузоред

# Иҷод кардани бот ва dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Ҷавоб ба фармони /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Салом! Ман боти оддӣ ҳастам!")

# Ҷавоб ба "Салом"
@dp.message_handler(lambda message: message.text.lower() == "салом")
async def echo_message(message: types.Message):
    await message.reply("Салом! Чӣ хабар? 😊")

# Иҷрои боти Telegram
if __name__ == '__main__':
    asyncio.run(dp.start_polling())
