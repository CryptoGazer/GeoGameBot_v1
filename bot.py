import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters import CommandStart

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart)
async def handle_start(message: Message):
    await message.answer("Hey!")



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.INFO("Bot is on!")
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.INFO("Bot is off!")

