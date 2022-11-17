"""
https://github.com/netology-code/pyfree-homeworks/blob/main/homeworks/5.md
Домашнее задание к занятию 5. Превращаем программу ToDo в бота
Задание 1

Расширьте функциональность бота возможностью на ваш выбор.
Примеры дополнительных возможностей:

    [+] 1) Выводить ошибку при добавлении задачи, в которой меньше 3х символов.
    [+] 2) Печатать задачи на несколько дат: принимать в команде show не одну дату, а произвольное количество.
    [в процессе] 3) При добавлении задачи учитывать отдельным параметром ее категорию. При выводе печатать категории задач со знаком @: Помыть посуду @Домашние дела.

Лучшие решения мы разберем на последнем занятии!
------------------------------------------

все изменения внесены в файл: 'bot-todo.py'
"""



"""
ОТВЕТ ДЛЯ 1

изменил функцию следующим образом:
одробнее смотреть в файле 'bot-todo.py'

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
"""


"""
ОТВЕТ ДЛЯ 2

изменил функцию следующим образом:
одробнее смотреть в файле 'bot-todo.py'

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
"""
