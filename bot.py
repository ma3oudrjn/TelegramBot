import telebot

# Initialize the bot with your Telegram API token
bot = telebot.TeleBot("YOUR_TELEGRAM_API_TOKEN")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Welcome to the bot! 😊")

@bot.message_handler(commands=['aboutus'])
def handle_aboutus(message):
    bot.reply_to(message, "We are a team dedicated to providing the best learning experience! 🚀")

@bot.message_handler(commands=['courses'])
def handle_courses(message):
    # Create a keyboard markup
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    backend_btn = telebot.types.KeyboardButton('Backend')
    frontend_btn = telebot.types.KeyboardButton('Frontend')
    sql_btn = telebot.types.KeyboardButton('SQL')
    markup.add(backend_btn, frontend_btn, sql_btn)

    bot.reply_to(message, 'Please select the course you are interested in:', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_selection(message):
    if message.text == 'Backend' or message.text == 'Frontend' or message.text == 'SQL':
        bot.reply_to(message, 'Please enter your name and surname along with your phone number.')
        # Save the user's input
        save_user_input(message.text, message.from_user.first_name, message.from_user.last_name, message.from_user.phone_number)
    else:
        bot.reply_to(message, 'Please select a valid course.')

def save_user_input(course, first_name, last_name, phone_number):
    # Add your code here to save the user's input
    print(f'Course: {course}\nFull Name: {first_name} {last_name}\nPhone Number: {phone_number}')

# Start the bot
bot.polling()