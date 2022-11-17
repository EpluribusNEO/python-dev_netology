"""
https://www.pythonanywhere.com/user/EPluribusNEO/files/home/EPluribusNEO
Домашнее задание к занятию 4. Создаем первого Telegram-бота
Задание 1

Модифицируйте нашего ЭхоБота таким образом, чтобы в ответ на сообщение, в котором присутствует ваше имя, он не повторял его, а отвечал: "Ба! Знакомые все лица!"
Подсказки

    Вам не нужно писать новых функций, достаточно модифицировать ту, что мы написали на занятии.
    Используйте конструкцию if word in string для того, чтобы проверить, входит ли слово word в строку string.

"""

import telebot
from os import environ
import dotenv

dotenv.load_dotenv('.env')
token = environ['APY_KEY']

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
	usr_name = message.from_user.first_name
	msg_from_usr = message.text
	msg_to_usr = ''
	if usr_name in msg_from_usr:
		msg_to_usr = 'Ба! Знакомые все лица!'
	else:
		msg_to_usr = msg_from_usr

	bot.send_message(message.chat.id, msg_to_usr)


bot.polling(none_stop=True)