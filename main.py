import random
import requests
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram Bot API token
BOT_TOKEN = 'YOUR_BOT_TOKEN'
# Replace 'YOUR_CAT_API_KEY' with your TheCatAPI API key
CAT_API_KEY = 'YOUR_CAT_API_KEY'

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I am your CatBot. Type /cat to see a random cat image.')

def cat(update: Update, context: CallbackContext) -> None:
    """Send a random cat image."""
    response = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={CAT_API_KEY}')
    if response.status_code == 200:
        cat_data = response.json()[0]
        cat_url = cat_data['url']
        update.message.reply_photo(photo=cat_url, caption='Here is a random cat image!')
    else:
        update.message.reply_text('Sorry, I couldn\'t fetch a cat image at the moment.')

def main() -> None:
    """Run the bot."""
    updater = Updater(BOT_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cat", cat))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
