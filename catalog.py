catalog_item = {
'type': 'phone', 
'vendor': 'Apple', 
'model': 'Iphone 7 black edition', 
'price': 37.5
}

catalog_item['audio_jack'] = False
catalog_item['price'] = 70

print(catalog_item['price'])

item_name = catalog_item['vendor'] + ' ' + catalog_item['model']

print(item_name)

print(catalog_item.get('price'))

print(catalog_item.get('discount', 'Скидок нет и не будет!'))


print(catalog_item)