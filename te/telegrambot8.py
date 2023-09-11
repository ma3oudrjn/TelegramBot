import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
from telegram.error import TelegramError

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token
TOKEN = ''

# Handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    # Creating the main menu
    main_menu_keyboard = [[InlineKeyboardButton("Courses", callback_data='courses'),
                          InlineKeyboardButton("About Us", callback_data='about_us')]]
    reply_markup = InlineKeyboardMarkup(main_menu_keyboard)
    
    # Sending the main menu
    update.message.reply_text("Welcome to the bot's menu!", reply_markup=reply_markup)

# Handler for the Courses menu
def handle_courses_menu(update: Update, context: CallbackContext) -> None:
    """Send a message when the 'Courses' menu option is selected."""
    courses_menu_keyboard = [[InlineKeyboardButton("Java Script", callback_data='javascript'),
                              InlineKeyboardButton("MySQL", callback_data='mysql'),
                              InlineKeyboardButton("Angular", callback_data='angular')]]
    reply_markup = InlineKeyboardMarkup(courses_menu_keyboard)

    # Sending the courses menu
    update.message.reply_text("Please select a course:", reply_markup=reply_markup)

# Handler for the callback queries
def button_click(update: Update, context: CallbackContext) -> None:
    """Handle button click events."""
    query = update.callback_query
    query.answer()

    # Sending the prompt for name and contact information
    query.message.reply_text("Please enter your name and contact information.")

    # Sending the user's response to the given Telegram ID
    response = f"Course: {query.data}\nUser's information: {query.message.text}"
    try:
        context.bot.send_message(chat_id='@Ma3oudRanjbaran', text=response)
    except TelegramError as e:
        logger.error(f"Failed to send message. Error: {e}")

# Create the updater and dispatcher
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("courses", handle_courses_menu))

# Add callback query handler
dispatcher.add_handler(CallbackQueryHandler(button_click))

# Start the bot
updater.start_polling()