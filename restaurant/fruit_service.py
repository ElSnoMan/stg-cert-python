from restaurant.datastore import Item, all_fruit_items


def get_all_fruits():
    return all_fruit_items


def get_fruit_by_name(name):
    for fruit in get_all_fruits():
        if name in fruit['name']:
            return fruit


def get_fruits_by_price(price):
    fruits = []
    for fruit in get_all_fruits():
        if price == fruit['price']:
            fruits.append(fruit)
    return fruits


def purchase_fruit(name, quantity):
    fruit = get_fruit_by_name(name)
    available = fruit['in_stock']
    if available < quantity:
        return f'{name}: Only {available} left'
    else:
        available -= quantity
    return f'Success: Ordered {quantity} {fruit["emoji"]}'
