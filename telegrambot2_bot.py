import telebot

bot_token = "5826178379:AAEg94X1NdN76lbLizrCCYYmPmE7kTTstgc"
bot = telebot.TeleBot(bot_token)

students = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Please register for the courses by providing your name.")

@bot.message_handler(func=lambda message: True)
def register_student(message):
    chat_id = message.chat.id
    if chat_id not in students:
        # Register student for the courses
        name = message.text
        students[chat_id] = {'name': name, 'courses': []}
        bot.reply_to(message, f"Hi {name}! Which courses would you like to register for? "
                              "Please choose from the following: Angular, Backend")
    else:
        # Add courses to the student's registration
        selected_courses = message.text.split(',')
        for course in selected_courses:
            course = course.strip().lower()
            if course == 'angular' or course == 'backend':
                students[chat_id]['courses'].append(course)
                bot.reply_to(message, f"You have been registered for {course.capitalize()} course.")
            else:
                bot.reply_to(message, f"Invalid course: {course}. Please select from Angular or Backend.")

@bot.message_handler(commands=['courses'])
def list_courses(message):
    bot.reply_to(message, "Courses available for registration: Angular, Backend")

@bot.message_handler(commands=['registered'])
def list_registered_students(message):
    response = "Registered students:\n"
    for chat_id, data in students.items():
        response += f"Chat ID: {chat_id}, Name: {data['name']}, Courses: {', '.join(data['courses'])}\n"
    bot.reply_to(message, response)

# Start the bot
bot.polling()