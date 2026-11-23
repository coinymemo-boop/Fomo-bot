import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 مرحبا بيك في Fomo Smart Bot\n\nهنا غادي نعاونك تعرف واش كاين FOMO في السوق ولا لا، باش ما تدخلش معطل.\n\nكتّب /help باش تشوف شنو كنقدر ندير.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "الأوامر المتوفرة:\n/start - البداية\n/help - المساعدة")

bot.infinity_polling()
