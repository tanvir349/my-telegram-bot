from telegram.ext import Updater, CommandHandler

TOKEN = "YOUR_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Hello! Bot is running 🚀")

def help_cmd(update, context):
    update.message.reply_text("Use /start")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_cmd))

updater.start_polling()
updater.idle()
