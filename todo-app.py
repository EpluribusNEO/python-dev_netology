import random

HELP = """
help - напечатать справку по программе.
add  - добавить задачу в список (название задачи запрашиваем у пользователя).
show - показать все добавленные задачи.
exit - Выход (закрыть программу)
random - Добавить случайную задачу на 'сегодня'"""

RANDOM_TASKS = ['Сыграть партейку в Контрушку', 'Выпить кофе', 'Покодить', 'Одохнуть', 'Погулять', 'Покушать', 'Погладить кота']


# Дана -> <задач>: {'31.12': ['Покатать в Контрушку', 'Покушать слатики', 'Послушать Путина']}
tasks = dict()


def add_new_task(date, task):
	if date in tasks:
		tasks[date].append(task)
	else:
		tasks[date] = []
		tasks[date].append(task)
	print(f"Задача '{task}' добавлена на дату '{date}'")

while True:
	command = input("Enter command:>")
	if command == 'help':
		print(HELP)
	elif command == 'add':
		date = input("Введите дату :>")
		task = input("Введите задачу:>")
		add_new_task(date,task)
	elif command == 'show':
		date = input("Введите дату для отображения:>")
		if date in tasks:
			print(f"Задачи на '{date}':")
			for task in tasks[date]:
				print(f"* {task}")
		else:
			print(f"Задач на '{date}' не найдено!")
	elif command == 'random':
		random_task = random.choice(RANDOM_TASKS)
		add_new_task('сегодня', random_task)

	elif command == 'exit':
		print('Прогарамма закрыта...')
		break
	else:
		print("[Предупреждение]: Неизвестная команда!")
		break

print("Спасибо за использование! До свидания!")
