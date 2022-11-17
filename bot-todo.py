import telebot
import dotenv
import random
from os import environ

HELP = """
/help - вывести справку по программе.
/add  - добавить задачу в список (/add <дата> <ваша задача>)
/show - показать задачи (/show <дата>)
/random - Добавить случайную задачу на 'сегодня'
/clear - Очистить весь список """

RANDOM_TASKS = ['Сыграть партейку в Контрушку', 'Выпить кофе', 'Покодить', 'Одохнуть', 'Погулять', 'Покушать',
                'Погладить кота']

dotenv.load_dotenv('.env')

token = environ['todo_bot_key']
bot = telebot.TeleBot(token)

tasks = dict()


def add_new_task(date, task):
	if date in tasks:
		tasks[date].append(task)
	else:
		tasks[date] = []
		tasks[date].append(task)


@bot.message_handler(commands=['add'])
def add(message):
	text = ''
	command = message.text.split(maxsplit=2)
	date = command[1].lower()
	task = command[2]
	if len(task) > 3:
		add_new_task(date, task)
		text = f"Задача '{task}' добавлена на дату '{date}'"
	else:
		text = f"Ошибка! Укажите задучу больше 3-х символов"
	bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def random_add(message):
	date = 'сегодня'
	task = random.choice(RANDOM_TASKS)
	add_new_task(date, task)
	text = f"Задача '{task}' добавлена на дату '{date}'"
	bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show'])
def show(message):
	text = 'Список дел'
	try:
		dates = message.text.split()  # [1].lower()
		for date in dates:
			text = text + f"\n\n___{date}___:\n"
			if date in tasks:
				for task in tasks[date]:
					text = text + f'[ ] {task}\n'
			else:
				text = f"Задач на дату '{date}' не найдено!"
	except:
		text = "Дата указана некорректно!\nиспользуйте запись /show <дата>"

	bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['clear'])
def clear(message):
	tasks.clear()
	bot.send_message(message.chat.id, 'список задач очищен')


@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, HELP)


bot.polling(none_stop=True)
