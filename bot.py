import os
import threading
import telebot
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Fomo Bot is running ✅"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 مرحبا بيك في Fomo Smart Bot\n\nهنا غادي نعاونك تعرف واش كاين FOMO في السوق ولا لا، باش ما تدخلش معطل.\n\nكتّب /help باش تشوف شنو كنقدر ندير.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "الأوامر المتوفرة:\n/start - البداية\n/help - المساعدة")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
