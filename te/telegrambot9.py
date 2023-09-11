import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

logging.basicConfig(level=logging.INFO)

TOKEN = '6301918114:AAHQZ1b7E6n_ybRJ9Zg0fZsbSP314_3pZUI'  # Replace with your bot token from BotFather
chat_id = None

def start(update, context):
    global chat_id
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, 'Welcome to our course selection bot!')

def courses(update, context):
    context.bot.send_message(chat_id, 'Course options: Java Script, MySQL, Angular')

def about_us(update, context):
    context.bot.send_message(chat_id, 'About us information goes here')

def handle_name(update, context):
    name = update.message.text
    context.bot.send_message(chat_id, f'Hello {name}! Your message has been received.')
    save_data(name)

def handle_phone(update, context):
    phone = update.message.text
    context.bot.send_message(chat_id, f'Thank you, {name}. We will contact you shortly.')
    save_data(phone)

def save_data(data):
    # Replace with your database connection code
    # For example, if using SQLite:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO data (name, phone) VALUES (?, ?)", (data,))
    conn.commit()
    conn.close()

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('courses', courses))
dispatcher.add_handler(CommandHandler('about_us', about_us))
dispatcher.add_handler(MessageHandler(Filters.text, handle_name))
dispatcher.add_handler(MessageHandler(Filters.text, handle_phone))

updater.start_polling()
updater.idle()