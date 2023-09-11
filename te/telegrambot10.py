import telebot
from telebot import types

# Create a Telegram bot
bot = telebot.TeleBot("6301918114:")

# Define the list of courses
courses = ["Python Programming", "Java Programming", "Data Science", "Machine Learning"]

# Define the function to handle the /start command
@bot.message_handler(commands=["start"])
def start(message):
   # Send a message to the user with the list of courses
   bot.send_message(message.chat.id, "Please select a course from the following list:\n\n" + "\n".join(courses))

# Define the function to handle the user's response
@bot.message_handler(func=lambda message: message.text in courses)
def course_selected(message):
   # Get the user's name and phone number
   bot.send_message(message.chat.id, "Please enter your name:")
   bot.register_next_step_handler(message, get_name)

def get_name(message):
   # Get the user's name
   name = message.text

   # Ask for the user's phone number
   bot.send_message(message.chat.id, "Please enter your phone number:")
   bot.register_next_step_handler(message, get_phone_number)

def get_phone_number(message):
   # Get the user's phone number
   phone_number = message.text

   # Save the user's information
   user_info = {
       "name": name,
       "phone_number": phone_number,
       "course": message.text
   }

   # Send a message to the user confirming their registration
   bot.send_message(message.chat.id, "Thank you for registering for the {} course! We will contact you soon.".format(message.text))

# Start the bot
bot.polling()