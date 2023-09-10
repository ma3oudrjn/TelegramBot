import telebot

bot_token = "5826178379:AAEg94X1NdN76lbLizrCCYYmPmE7kTTstgc"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    # Handle the start command
    bot.reply_to(message, "Hello! How can I assist you?")

@bot.message_handler(commands=['about us'])
def about_us(message):
    # Handle the about us command
    bot.reply_to(message, "We are a team of programmers.")

@bot.message_handler(commands=['help'])
def help(message):
    # Handle the help command
    bot.reply_to(message, "How can I help you?")

@bot.message_handler(commands=['courses'])
def courses(message):
    # Handle the courses command
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    backend_btn = telebot.types.KeyboardButton('backend')
    front_btn = telebot.types.KeyboardButton('front')
    sql_btn = telebot.types.KeyboardButton('sql')
    keyboard.add(backend_btn, front_btn, sql_btn)
    bot.reply_to(message, "Please select a course:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def save_message(message):
    # Save user message
    # You can implement your own logic to save the message
    saved_message = message.text
    print("Saved message:", saved_message)

    # Reply with a confirmation message
    bot.reply_to(message, "Your message has been saved!")

@bot.message_handler(func=lambda message: message.text == 'backend' or message.text == 'front' or message.text == 'sql')
def handle_course_selection(message):
    # Handle course selection
    bot.reply_to(message, "esm o famil be hamrah shomare ra vared konid")

# Start the bot
bot.polling()