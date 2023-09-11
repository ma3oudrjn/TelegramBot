import telebot

bot_token = "6301918114:AAHQZ1b7E6n_ybRJ9Zg0fZsbSP314_3pZUI"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    menu = create_menu()
    bot.send_message(message.chat.id, "hi welcome to faradid bot", reply_markup=menu)

def create_menu():
    menu = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    courses_btn = telebot.types.KeyboardButton('Courses')
    aboutus_btn = telebot.types.KeyboardButton('About Us')
    menu.add(courses_btn, aboutus_btn)
    return menu

@bot.message_handler(func=lambda message: message.text == 'Courses')
def courses_menu(message):
    menu = create_courses_menu()
    bot.send_message(message.chat.id, "Please select a course:", reply_markup=menu)

def create_courses_menu():
    menu = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    js_btn = telebot.types.KeyboardButton('JavaScript')
    mysql_btn = telebot.types.KeyboardButton('MySQL')
    angular_btn = telebot.types.KeyboardButton('Angular')
    menu.add(js_btn, mysql_btn, angular_btn)
    return menu

@bot.message_handler(func=lambda message: message.text in ['JavaScript', 'MySQL', 'Angular'])
def ask_user_info(message):
    course = message.text
    bot.send_message(message.chat.id, "Please enter your name and contact information:")
    bot.register_next_step_handler(message, save_user_info, course)

def save_user_info(message, course):
    name_contact = message.text.split('\n')
    name = name_contact[0]
    contact = name_contact[1]
    user_info = f"Course: {course}\nName: {name}\nContact: {contact}\nUser Message: {message.text}"
    bot.send_message("@Ma3oudRanjbaran", user_info)

@bot.message_handler(func=lambda message: message.text == 'About Us')
def about_us(message):
    bot.reply_to(message, "We are an awesome organization. Here is some information about us...")

# Start the bot
bot.polling()