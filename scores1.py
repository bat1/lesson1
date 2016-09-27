scores_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '9b', 'scores': [5,4,3,5,5]},{'school_class': '3c', 'scores': [3,3,2,2,3]}]
dict_4a = (scores_list[0])
dict_9b = (scores_list[1])
dict_3c = (scores_list[2])
all_scool_scores = dict_4a.get('scores') + dict_9b.get('scores') + dict_3c.get('scores') #делаем единиый список омценок со всех классов
average_school_scores = (sum(all_scool_scores)/len(all_scool_scores)) #находим среднюю оценку по школе
print("Средняя оценка по всей школе составляет: " + str(average_school_scores))
list_4a = dict_4a.get('scores') #выделяем список оценок по 4а классу
list_9b = dict_9b.get('scores') #выделяем список оценок по 9b классу
list_3c = dict_3c.get('scores') #выделяем список оценок по 3с классу
print("Средняя оценка в 4а классе равна: " + str(sum(list_4a) / len(list_4a)))
print("Средняя оценка в 9b классе равна: " + str(sum(list_9b) / len(list_9b)))
print("Средняя оценка в 3с классе равна: " + str(sum(list_3c) / len(list_3c)))