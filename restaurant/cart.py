from restaurant.fruit_service import purchase_fruit


cart_items = [
    {'name': 'Mango', 'quantity': 10},
    {'name': 'Apple', 'quantity': 5},
    {'name': 'Peach', 'quantity': 2}
]


def place_order():
    for item in cart_items:
        response = purchase_fruit(item['name'], item['quantity'])
        if 'Success' in response:
            cart_items.remove(item)
        else:
            print('do something else...')
