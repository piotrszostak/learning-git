shopping_list = {
    'piekarnia' : ['chleb', 'bułki', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}

for shop, products in shopping_list.items():
    items_capitalized = []
    for item in products:
        items_capitalized.append(item.capitalize())
    print(f"Idę do {shop.capitalize()} i kupuję tam: {items_capitalized}.")

bake_items = len(shopping_list['piekarnia'])
veg_items = len(shopping_list['warzywniak'])

sum_items = bake_items + veg_items
print(f"W sumie kupuję {sum_items} produktów.")

