from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler
import os
from repositories import get_all_repositories

# token = os.environ['TELEGRAM_BOT_API']

# app = ApplicationBuilder().token(token).build()

print('Bot started')
print(get_all_repositories())