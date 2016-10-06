from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from answers import get_answer, answers
import ephem

dict_nums_to_words = {'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 
'пять': '5', 'шесть': '6', 'семь': '7', 'восемь': '8', 'девять': '9', 'десять': '10'}

dict_actions = {'умножить': '*', 
	'прибавить': '+', 'плюс': '+', 'минус': '-', 'отнять': '-', 'разделить': '/', 'делить': '/'}

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text='Привет, человек! Я бот, который помогает учиться на курсе Learn Python')

def count(bot, update):
	bot.sendMessage(update.message.chat_id, text=('В фразе' + ' ' + '"' + update.message.text[7:] + '"' + ':' +  ' ' + '{}'.format(count_words(update.message.text[7:])) + ' ' + 'слова')) #Отвечаем сколько слов в сторке, которую вводит пользователь

def icalc(bot, update):
	print("Вызван /icalc")
	bot.sendMessage(update.message.chat_id, text='Привет, человек! Я стал еще умнее! \nХочешь узнать сколько будет' + ' '+ '"' + update.message.text[21:] + '"' + '?' + ' ' + '\nОтвечаю: ' + '{}'.format(actions(calc_words(update.message.text[7:])))) #Считаем арифметические операции сказанные фразами вида "сколль будет два плюс три"

def calc(bot, update):
	print("Вызван /calc")
	bot.sendMessage(update.message.chat_id, text='Привет! Я бот - калькулятор, делаю вычисления с помощью нейронных сетей, квантовых процессоров и прочей фигни! Хочешь знать сколько будет' + ' ' + '"' + update.message.text[5:] + '"' + '?' +  ' ' + 'Отвечаю:' + '{}'.format(calc_num(update.message.text[5:]))) #Считаем арифметические операции


def ephem_moon(bot, update):
	print("Вызван /ephem_moon")
	moon = find_fool_moon(update.message.text)
	bot.sendMessage(update.message.chat_id, text='Привет, человек! \nТы спрашиваешь: "{}"? \nОтвечаю: {}'.format(update.message.text[12:], moon)) #Считаем дату ближайшей полной луны после указанной в тексте датой

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

	if '-' in flatten:
		number1 = flatten[0]
		number2 = flatten[2]
		difference = int(number1) - int(number2)
		return difference

	if '*' in flatten:
		number1 = flatten[0]
		number2 = flatten[2]
		composition = int(number1) * int(number2)
		return composition

	if '/' in flatten:
		number1 = flatten[0]
		number2 = flatten[2]
		division = int(number1) / int(number2)
		return division

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

def find_fool_moon(text, date='2016-10-01'):

	if date in text:
		date = date.replace('-', '/')
		print(date)
		fool_moon = ephem.next_full_moon(date)
	return 'Следующая дата полнолуния: {}'.format(fool_moon)

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
    	print('Ошибка Unauthorized')
        # remove update.message.chat_id from conversation list
    except BadRequest:
    	print('Ошибка BadRequest')
        # handle malformed requests - read more below!
    except TimedOut:
    	print('Ошибка TimedOut')
        # handle slow connection problems
    except NetworkError:
    	print('Ошибка NetworkError')
        # handle other connection problems
    except ChatMigrated as e:
    	print('Ошибка ChatMigrated')
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
    	print('Ошибка TelegramError')
        # handle all other telegram related errors


def run_bot():
	updater = Updater("272924743:AAEjalIxbPU2Pjb0Q4TrCM9oqrqUyZ3tYCY")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("count", count))
	dp.add_handler(CommandHandler("calc", calc))
	dp.add_handler(CommandHandler("icalc", icalc))
	dp.add_handler(CommandHandler("ephem_moon", ephem_moon))
	dp.add_error_handler(error_callback)
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':

	run_bot()
	calc_num(text)
	calc_words(text)
	actions(flatten)

