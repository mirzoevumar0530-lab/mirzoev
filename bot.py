# bot.py
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import os

# Token-ро аз файли token.txt мехонем
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Ҳар вақте корбар /start менависад
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Салом! Ман боти калкулятор ҳастам.\nЛутфан масъалаи худро мисли '2 + 3 * 5' ворид кунед:")

# Ҳар паёми матнӣ ҳамчун масъала қабул мешавад
@dp.message()
async def calc_handler(message: Message):
    expr = message.text.strip()
    try:
        # Амалиёти хатарноки eval-ро муҳофизат мекунем
        allowed_chars = "0123456789+-*/(). "
        if any(c not in allowed_chars for c in expr):
            raise ValueError("Намунае нодуруст!")
        result = eval(expr)
        await message.answer(f"{expr} = {result}")
    except Exception:
        await message.answer("Хатогӣ: Лутфан танҳо амалиётҳои математикӣ ворид кунед (мисол: 2 + 3 * 5)")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
