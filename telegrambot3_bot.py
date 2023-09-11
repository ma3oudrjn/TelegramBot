import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# States
NAME, PHONE, COURSE = range(3)

# Dictionary to store user data
user_data = {}

# Command handler for /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_html(
        fr"Hi {user.mention_html()}!",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton('/aboutUs'), KeyboardButton('/courses')]],
            resize_keyboard=True,
        ),
    )

# Command handler for /aboutUs
def about_us(update: Update, context: CallbackContext):
    update.message.reply_text("We are a tech education platform!")

# Command handler for /courses
def courses(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("Angular"), KeyboardButton("SQL"), KeyboardButton("YouTube")],
    ]
    update.message.reply_text("Select a course:", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return COURSE

# Function to handle selected course
def select_course(update: Update, context: CallbackContext):
    user = update.message.from_user
    course = update.message.text
    user_data['course'] = course
    update.message.reply_text(f"You've selected the {course} course.")
    update.message.reply_text("Please provide your name:")
    return NAME

# Function to handle user name
def receive_name(update: Update, context: CallbackContext):
    user = update.message.from_user
    name = update.message.text
    user_data['name'] = name
    update.message.reply_text(f"Thanks, {name}! Please provide your phone number:")
    return PHONE

# Function to handle user phone number
def receive_phone(update: Update, context: CallbackContext):
    user = update.message.from_user
    phone_number = update.message.text
    user_data['phone_number'] = phone_number

    # Save user data (you can modify this part to save data in a database)
    with open('user_data.txt', 'a') as file:
        file.write(f"Name: {user_data['name']}, Phone: {phone_number}, Course: {user_data['course']}\n")

    update.message.reply_text("Thank you! Your information has been saved.")
    return ConversationHandler.END

# Function to cancel the conversation
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END

def main():
    # Your Telegram Bot API token
    token = "5826178379:AAEg94X1NdN76lbLizrCCYYmPmE7kTTstgc"

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            COURSE: [MessageHandler(filters.regex('^(Angular|SQL|YouTube)$'), select_course)],
            NAME: [MessageHandler(filters.text & ~filters.command, receive_name)],
            PHONE: [MessageHandler(filters.text & ~filters.command, receive_phone)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler('aboutUs', about_us))
    dispatcher.add_handler(CommandHandler('courses', courses))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
