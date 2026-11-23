import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message, "سلام! أنا Fomo Smart Bot خدام ✅")

@bot.message_handler(func=lambda m: True)
def echo(message):
 bot.reply_to(message, "وصلاتني")

bot.infinity_polling()

3. هبط لتحت كاع وورك على *Commit changes*

ملي تسالي، قولي ليا `صايبت bot.py` باش نزيدو الملف الثاني `requirements.txt`.
