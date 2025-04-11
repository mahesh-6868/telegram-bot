from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

TOKEN = "7760147090:AAHoPCvaBBraczMSX_tVmTnWc3I4OUa9uxM"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Send me any message, and I'll reply!")

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = f"You said: {user_message}"
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()