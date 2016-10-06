import ephem

dict_nums_to_words = {'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 
'пять': '5', 'шесть': '6', 'семь': '7', 'восемь': '8', 'девять': '9', 'десять': '10'}

dict_actions = {'умножить': '*', 
	'прибавить': '+', 'плюс': '+', 'минус': '-', 'отнять': '-', 'разделить': '/', 'делить': '/'}


def calc_words(text):

	separated_words = text.split()
	flatten = []

	for item in separated_words:
		num = dict_nums_to_words.get(item)
		if num:
				flatten.append(num)
		action = dict_actions.get(item)
		if action:
				flatten.append(action)
	return flatten

def actions(flatten):

	if '+' in flatten:
		number1 = flatten[0]
		number2 = flatten[2]
		sum_numbers = int(number1) + int(number2)
	return sum_numbers

print(calc_words('сколько будет два плюс три'))
print(actions(['2','+','3']))


def find_fool_moon(text):
	
	date = '2016-10-01'
	if date in text:
		date = date.replace('-', '/')
		date_next_full_moon = ephem.next_full_moon(date)
	return date_next_full_moon

print(find_fool_moon('Когда ближайшее полнолуние после 2016-10-01?'))


#	if item in separated_words:
#		num1, num2 = dict_nums_to_words.get(item)
#		print(num1 + num2)
#		return summa

#	if item in separated_words:
#		action = dict_actions.get(item)
#		print(action)
#		return action

#	calc_num(text)



#dict_keys(['плюс', 'разделить', 'умножить на', 'делить', 'прибавить', 'отнять', 'минус'])
#['сколько', 'будет', 'два', 'плюс', 'три']