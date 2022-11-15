

def fact(n):
	if n > 0:
		return n * fact(n - 1)
	elif n == 0:
		return 1
	else:
		return 0


if __name__ == '__main__':
	print("___TESTING___")
	numb = int(input("Enter value:> "))
	print(f"{numb}! = {fact(numb)}")