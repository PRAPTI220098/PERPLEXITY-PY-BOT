import os
import telebot
from telebot import types
import requests
from datetime import datetime, timedelta
import flask
from user_agent import generate_user_agent as rrr
from perplexityai import Perplexity

tk = os.environ.get('BOT_TOK')
bot = telebot.TeleBot(tk)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    usr = message.from_user.first_name
    text = f"Hey, [{usr}](tg://settings)!\n\n🌐_Welcome to Perplexity Ai – Your AI Powerhouse!_ 🤖.\n\n✨_Ask anything for real-time knowledge, latest news, and expert insights. Stay informed, stay sharp! 💡🌍_ \n#SmartBot"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    dev = types.InlineKeyboardButton(text='💸 SANCHIT 💸', url='https://t.me/X668F')
    ista = types.InlineKeyboardButton(text='🔮 Follow Me On Instagram 🔮', url='https://www.instagram.com/sanch1t')
    keyboard.add(dev,ista)
    bot.send_message(message.chat.id, text, parse_mode='markdown', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def ru(message):
    uid = message.from_user.id
    un = message.from_user.first_name
    w = bot.send_message(message.chat.id, "<i>🔍 Searching On It...</i>", parse_mode='HTML')    
    text = message.text
    res = chatbot(text)
    bot.delete_message(message.chat.id, w.message_id)
    bot.send_message(message.chat.id, f"{res}", parse_mode='markdown')


def chatbot(text):
  ans = list(Perplexity().generate_answer(text))
  s = len(ans) - 1
  ss = ans[s]['answer']
  rr= ss.split('[')[0].strip()
  return f"{rr}"

bot.infinity_polling()
