text = '2/3'
words = 'сколько будет два плюс три'

dict_nums_to_words = {'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 
'пять': '5', 'шесть': '6', 'семь': '7', 'восемь': '8', 'девять': '9', 'десять': '10', 'умножить на': '*', 
'прибавить': '+', 'плюс': '+', 'минус': '-', 'отнять': '-', 'разделить на': '/', 'делить на': '/'}

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

def calc_word(words):
	words = 'сколько будет два плюс три'
	one_word = words.split()
	for one_word[] in dict_nums_to_words:
		number1, number2 = dict_nums_to_words.get(one_word)
		summa = int(number1) + int(number2)
		print(summa)
		return summa


if __name__ == '__main__':

	calc('text')
	calc_word(words)
