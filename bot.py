from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text='Привет, человек! Я бот, который помогает учиться на курсе Learn Python')

def count(bot, update):
	bot.sendMessage(update.message.chat_id, text=('В фразе' + ' ' + '"' + update.message.text[7:] + '"' + ':' +  ' ' + str(count_words(update.message.text[7:])) + ' ' + 'слова')) #Отвечаем сколько слов в сторке, которую вводит пользователь


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
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':

	run_bot()