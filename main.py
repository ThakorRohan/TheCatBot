import requests
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, CallbackContext
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')
CAT_API_KEY = config('CAT_API_KEY')

async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hello! I am your CatBot. Type /cat to see a random cat image.')

async def cat(update: Update, context: CallbackContext) -> None:
    """Send a random cat image."""
    response = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={CAT_API_KEY}')
    if response.status_code == 200:
        cat_data = response.json()[0]
        cat_url = cat_data['url']
        await update.message.reply_photo(photo=cat_url, caption='Here is a random cat image!')
    else:
        await update.message.reply_text('Sorry, I couldn\'t fetch a cat image at the moment.')

def main() -> None:
    """Run the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    cat_handler = CommandHandler("cat", cat)

    application.add_handler(start_handler)
    application.add_handler(cat_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
