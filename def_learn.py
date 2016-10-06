




def get_vat(payment, percent=18):
	try:
		payment = float(payment)
		percent = int(percent)
		vat = payment / 100 * percent
		vat = round(vat, 2)
		return 'Сумма НДС: {}'.format(vat)
	except (TypError, ValueError):
		print('Не правильный формат данных, введите сумму!')

result = get_vat(400, 10)
print(result)
