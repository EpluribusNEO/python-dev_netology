"""
TODO Домашнее задание к занятию 2. Первая программа
Продолжим совершенствовать наше ToDo приложение.
https://github.com/netology-code/pyfree-homeworks/blob/main/homeworks/2.md
"""

"""
Задание 1

Модифицируйте программу, написанную на занятии так,
чтобы выход из нее осуществлялся не только при вводе неизвестной команды,
но и при вводе специальной команды exit.
Сделайте так, чтобы при вводе этой команды программа выводила на экран текст: "Спасибо за использование! До свидания!"

Пример ввода-вывода программы:
Введите команду
exit
Спасибо за использование! До свидания!
"""

"""
Задание 2

Давайте усложним нашу программу. Сделайте следующие изменения:

    Заведите 3 списка: today, tomorrow, other (вы можете назвать переменные по-другому).
    Измените блок кода, который выполняет команду add:

    Дополнительно запросите у пользователя дату выполнения задачи.
    В зависимости от введенной даты добавьте задачу в один из списков по следующим правилам:
        Если пользователь ввел "Сегодня", добавьте задачу в список today.
        Если пользователь ввел "Завтра", добавьте задачу в список tomorrow.
        Если пользователь ввел любое другое значение, добавьте задачу в список other.
"""



# <Задание 1>
print("\n\nЗадание 1")
HELP = """
help - напечатать справку по программе.
add  - добавить задачу в список (название задачи запрашиваем у пользователя).
show - показать все добавленные задачи.
exit - Выход (закрыть программу)"""
tasks = []

while True:
	command = input("Enter command:>")
	if command == 'help':
		print(HELP)
	elif command == 'add':
		task = input("Enter task name:>")
		tasks.append(task)
		print("Task was add to task list...")
	elif command == 'show':
		print(tasks)
	elif command == 'exit':
		print('Прогарамма закрыта...')
		break
	else:
		print("[Warning]: Unknown commnad!")
		break

print("Спасибо за использование! До свидания!")
# </Задание 1>



# <Задание 2>
print("\n\nЗадание 2")
HELP = """
help - напечатать справку по программе.
add  - добавить задачу в список (указать <Дату> и <Что сделать>).
show - показать все добавленные задачи.
exit - Выход (закрыть программу)"""
tasks_today = []
tasks_tomorrow = []
tasks_other = []

while True:
	command = input("Введите команду:>")
	if command == 'help':
		print(HELP)
	elif command == 'add':
		date = input("Ведите дату (сегодня, завтра, <Свой вариант>) :> ")
		task = input("Введите задачу:>")
		if date.lower() == "сегодня":
			tasks_today.append(task)
		elif date.lower() == "завтра":
			tasks_tomorrow.append(task)
		else:
			tasks_other.append(task)
		print("Задача добавлена")
	elif command == 'show':
		if len(tasks_today) > 0:
			print("Сегодня:", tasks_today)
		if len(tasks_tomorrow) > 0:
			print("Завтра:", tasks_tomorrow)
		if len(tasks_other) > 0:
			print("Остальные:", tasks_other)
	elif command == 'exit':
		print('Прогарамма закрыта...')
		break
	else:
		print("[Warning]: Неизвестная команда!")
		break

print("Спасибо за использование! До свидания!")
# </Задание 2>