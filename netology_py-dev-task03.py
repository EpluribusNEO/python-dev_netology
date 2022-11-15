"""
TODO Задание 1

Реализуйте функцию count_letter,
которая принимает список слов и некоторую букву
и возвращает количество слов в списке,
в которых эта буква встречается хотя бы один раз.

Например, для списка ['python', 'c++', 'c', 'scala', 'java'] и буквы 'c' ваша функция должна вернуть число 3.
Подсказки

    Используйте конструкцию for word in ... для итерации по списку.
    Используйте переменную для хранения промежуточного результата подсчета.
    Используйте конструкцию letter in word для проверки наличия буквы в слове.

"""

"""
TODO Задание 2

Зарегистрируйтесь на сайте https://www.pythonanywhere.com/.
Инструкция

Инструкция по работе с PythonАnywhere доступна по ссылке: https://github.com/netology-code/guides/blob/master/python%20anywhere/instruction.md
"""

# <Задание 1>
DEFAULT_LIST = ['python', 'c++', 'c', 'scala', 'java']
DEFAULT_CHAR = 'c'

def count_letter(words, char):
	count = 0
	for word in words:
		for letter in word:
			if letter == char:
				count = count + 1
	return count
# </Задание 1>

if __name__ == '__main__':
	my_list = ['хлеб', 'огурчики', 'горошек', 'яйца', 'мясо', 'картофель', 'морковка', 'майонез', 'соль']
	find_char = input("Введите символ для поиска:>")
	count = count_letter(my_list, find_char)
	print(f"Символ '{find_char}' встречается {count} раз")


# <Задание 2>
# ЗАРГИСТРИРОВАЛСЯ НА https://www.pythonanywhere.com
# Инструкция по работе с PythonАnywhere доступна по ссылке (ниже):
# https://github.com/netology-code/guides/blob/master/python%20anywhere/instruction.md
# </Задание 2>
