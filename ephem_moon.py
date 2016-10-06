import ephem

def find_fool_moon(text, date='2016-10-01'):

	if date in text:
		date = date.replace('-', '/')
		print(date)
		fool_moon = ephem.next_full_moon(date)
	return 'Следующая дата полнолуния: {}'.format(fool_moon)


print(find_fool_moon('Когда ближайшее полнолуние после 2016-10-01?'))