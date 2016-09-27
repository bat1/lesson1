mylist = ['Вася', 'Валера', 'Петя', 'Валера', 'Саша', 'Даша']
count = 0
while count < len(mylist):
	if mylist.pop([count]) == 'Валера':
		print('Валера нашелся')
		break
	count += 1
