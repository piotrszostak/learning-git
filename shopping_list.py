shopping_list = {
    'piekarnia' : ['chleb', 'bułki', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}

for shop, products in shopping_list.items():
    items_capitalized = []
    for item in products:
        items_capitalized.append(item.capitalize())
    print(f"Idę do {shop.capitalize()} i kupuję tam: {items_capitalized}.")

sum = len(shopping_list['piekarnia']) + len(shopping_list['warzywniak'])
print(f"W sumie kupuję {sum} produktów.")

