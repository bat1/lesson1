answers = {'привет': 'И тебе привет', 'как дела?': 'Лучше всех!', 'пока': 'Увидимся'}


def get_answer(question, answers):
	return answers.get(question)

def ask_user(answers):
	while True:
		user_input = input('Скажи что нибудь:')
		answer = get_answer(user_input, answers)
		print(answer)

		if user_input == 'пока':
			break

ask_user(answers)