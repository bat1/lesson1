from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text='Привет, человек! Я бот, который помогает учиться на курсе Learn Python')

def count(bot, update):
	bot.sendMessage(update.message.chat_id, text=('В фразе' + ' ' + '"' + update.message.text[7:] + '"' + ':' +  ' ' + str(count_words(update.message.text[7:])) + ' ' + 'слова')) #Отвечаем сколько слов в сторке, которую вводит пользователь

def calc(bot, update):
	print("Вызван /calc")
	bot.sendMessage(update.message.chat_id, text='Привет! Я бот - калькулятор, делаю вычисления с помощью нейронных сетей, квантовых процессоров и прочей фигни! Хочешь знать сколько будет' + ' ' + '"' + update.message.text[5:] + '"' + '?' +  ' ' + '\nОтвечаю: ' + str(calc_num(update.message.text[5:]))) #Считаем арифметические операции

#def calc_num(bot, update):


def calc_num(text):

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

def talk_to_me(bot, update):
	print("Пришло сообщение: " + update.message.text)
	bot.sendMessage(update.message.chat_id, text=(update.message.text)) #Отвечаем то же самое, что написал человек.

def count_words(text):
	num_words = len(text.split())
	return num_words

def run_bot():
	updater = Updater("272924743:AAEjalIxbPU2Pjb0Q4TrCM9oqrqUyZ3tYCY")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("count", count))
	dp.add_handler(CommandHandler("calc", calc))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':

	run_bot()
	calc_num(text)