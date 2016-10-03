print("Hello, world")
a = 1
b = 2
c = a + b
print(c)

dict_nums_to_words = {'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 
'пять': '5', 'шесть': '6', 'семь': '7', 'восемь': '8', 'девять': '9', 'десять': '10'}
dict_operations = {'умножить на': '*', 
'прибавить': '+', 'плюс': '+', 'минус': '-', 'отнять': '-', 'разделить на': '/', 'делить на': '/'}

words = 'сколько будет два плюс три'
one_word = words[13:].split()
for item in one_word:
	num1, num2 = dict_nums_to_words.get(item)
	print(num1)
	print(num2)
	action = dict_operations.get(item)
	print(action)



