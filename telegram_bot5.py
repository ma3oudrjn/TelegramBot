import telebot

bot_token = "6301918114:AAHQZ1b7E6n_ybRJ9Zg0fZsbSP314_3pZUI"
bot = telebot.TeleBot(bot_token)

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in users:
        users[chat_id] = {'name': '', 'contact': ''}
        bot.send_message(chat_id, "Welcome! Please choose an option from the menu.", reply_markup=generate_menu())    
    else:
        bot.send_message(chat_id, "You are already registered. Please choose an option from the menu.", reply_markup=generate_menu())

@bot.message_handler(commands=['aboutus'])
def about_us(message):
    bot.reply_to(message, "We are an awesome organization. Here is some information about us...")

def generate_menu():
    menu = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    courses_btn = telebot.types.KeyboardButton('Courses')
    aboutus_btn = telebot.types.KeyboardButton('About Us')
    menu.add(courses_btn, aboutus_btn)
    return menu

@bot.message_handler(func=lambda message: message.text == 'Courses')
def show_courses_menu(message):
    chat_id = message.chat.id
    courses_menu = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    js_btn = telebot.types.KeyboardButton('JavaScript')
    mysql_btn = telebot.types.KeyboardButton('MySQL')
    angular_btn = telebot.types.KeyboardButton('Angular')
    courses_menu.add(js_btn, mysql_btn, angular_btn)
    bot.send_message(chat_id, "Please select a course:", reply_markup=courses_menu)

@bot.message_handler(func=lambda message: message.text in ['JavaScript', 'MySQL', 'Angular'])
def ask_user_info(message):
    chat_id = message.chat.id
    course = message.text
    users[chat_id]['course'] = course
    bot.send_message(chat_id, "Please enter your name and contact information:")
    bot.register_next_step_handler(message, save_user_info)

def save_user_info(message):
    chat_id = message.chat.id
    name_contact = message.text.split('\n')
    name = name_contact[0]
    contact = name_contact[1]
    users[chat_id]['name'] = name
    users[chat_id]['contact'] = contact
    bot.send_message(chat_id, "Thank you for providing your information!")

@bot.message_handler(func=lambda message: True)
def save_message(message):
    chat_id = message.chat.id
    if chat_id in users:
        saved_message = message.text
        users[chat_id]['message'] = saved_message
        print("User Information:", users[chat_id])
        bot.send_message(chat_id, "Your message has been saved!")

# Start the bot
bot.polling()