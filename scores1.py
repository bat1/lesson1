scores_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '9b', 'scores': [5,4,3,5,5]},{'school_class': '3c', 'scores': [3,3,2,2,3]}]

new_school_class = input('Input a name of new schooll class: ')

list_new_school_class = []

for student_num in range(5):
    student_score = int(input('Введите оценку ученика: '))
    list_new_school_class.append(student_score)

dict_new_school_class = dict(school_class=new_school_class, scores=list_new_school_class) #создаем словарь с оценками нового класса
scores_list.append(dict_new_school_class) #добавляем словарь нового класса в список оценок

#Теперь попробуй считать оценки классов в цикле: обойдись без переменных с названиями классов.

flatten = []
for item in scores_list:
	class_number = str(item.get('school_class'))
	score = item.get('scores')
	flatten.extend(score)
	print('Средняя оценка в классе' + ' ' + class_number + ' ' + 'равна: ' + str(sum(score) / len(score)))
	print('Средняя оценка по школе равна: ' + str(sum(flatten) / len(flatten)))