def cut_cake(parts):
	try:
		return 1 / int(parts)
	except (ZeroDivisionError):
		return "С ума посходили что ли? Делить на ноль нельзя!"
	except (TypeError, ValueError):
		return "Хм... зачем вводишь белиберду? Введите целое число!"
cake = int(cut_cake("1"))
print("Пирог разделен на" + " " + str(cake) + " " + "кусков!")

def do_smth(x):
	try:
		print(x)
	except:
		print('Пока!')
x = 0
while x < 10:
	do_smth(x)
x += 1