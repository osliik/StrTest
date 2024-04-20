import telebot
from pymongo import MongoClient
from datetime import datetime

TOKEN = '7106009428:AAGcuetQwzivdmT-BlzY8BHl4mRDlO6-axk'

client = MongoClient('mongodb://localhost:27017/')
db = client['telegram_bot']
collection = db['messages']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    message_text = message.text
    message_date = datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S')
    collection.insert_one({'text': message_text, 'date': message_date})
    
    response = "Strattonbot {}".format(message_text)
    bot.send_message(message.chat.id, response)

bot.polling()
