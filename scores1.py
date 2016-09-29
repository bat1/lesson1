scores_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '9b', 'scores': [5,4,3,5,5]},{'school_class': '3c', 'scores': [3,3,2,2,3]}]

new_school_class = input('Input a name of new schooll class: ')

list_new_school_class = []
for student_num in range(4):
    student_score = int(input('Введите оценку ученика: '))
    list_new_school_class.append(student_score)

#Теперь попробуй считать оценки классов в цикле: обойдись без переменных с названиями классов.

dict_new_school_class = {'school_class': str(new_school_class), 'scores': list_new_school_class} #создаем словарь с оценками нового класса
scores_list.extend(dict_new_school_class) #добавляем словарь нового класса в список оценок

dict.values({scores_list[0:3]})


all_school_scores = dict_4a.get('scores') + dict_9b.get('scores') + dict_3c.get('scores') + list_new_school_class  #делаем единиый список омценок со всех классов

average_school_scores = sum(all_school_scores) / len(all_school_scores) #находим среднюю оценку по школе

print("Средняя оценка по всей школе составляет: " + str(average_school_scores))

list_4a = dict_4a.get('scores') #выделяем список оценок по 4а классу
list_9b = dict_9b.get('scores') #выделяем список оценок по 9b классу
list_3c = dict_3c.get('scores') #выделяем список оценок по 3с классу

print("Средняя оценка в 4а классе равна: " + str(sum(list_4a) / len(list_4a)))
print("Средняя оценка в 9b классе равна: " + str(sum(list_9b) / len(list_9b)))
print("Средняя оценка в 3с классе равна: " + str(sum(list_3c) / len(list_3c)))
print("Средняя оценка в" + " " + new_school_class + " " + "классе равна: " + str(sum(list_new_school_class) / len(list_new_school_class)))