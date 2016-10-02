text = "2/3"

def calc(text):

	if '+' in text:
		number1, number2 = text.split('+')
		sum_numbers = int(number1) + int(number2)
		print(sum_numbers)
		return sum_numbers

	if '-' in text:
		number1, number2 = text.split('-')
		difference = int(number1) - int(number2)
		print(difference)
		return difference

	if '*' in text:
		number1, number2 = text.split('*')
		composition = int(number1) * int(number2)
		print(composition)
		return composition

	if '/' in text:
		number1, number2 = text.split('/')
		division = int(number1) / int(number2)
		print(division)
		return division

calc(text)