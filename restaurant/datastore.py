# emojis from https://unicode.org/emoji/charts/full-emoji-list.html
from pydantic import BaseModel


class Item(BaseModel):
    ID: int
    name: str
    emoji: str
    in_stock: int
    price: float


all_fruit_items = [
    {
        'ID': 1,
        'name': 'grapes',
        'emoji': '🍇',
        'in_stock': 22,
        'price': 0.50
    },
    {
        'ID': 2,
        'name': 'melon',
        'emoji': '🍈',
        'in_stock': 10,
        'price': 1.00
    },
    {
        'ID': 10,
        'name': 'green apple',
        'emoji': '🍏',
        'in_stock': 120,
        'price': 0.50
    },
    {
        'ID': 3,
        'name': 'watermelon',
        'emoji': '🍉',
        'in_stock': 2,
        'price': 2.50
    },
    {
        'ID': 4,
        'name': 'tangerine',
        'emoji': '🍊',
        'in_stock': 1,
        'price': 1.50
    },
    {
        'ID': 5,
        'name': 'lemon',
        'emoji': '🍋',
        'in_stock': 100,
        'price': 0.25
    },
    {
        'ID': 6,
        'name': 'banana',
        'emoji': '🍌',
        'in_stock': 12,
        'price': 1.50
    },
    {
        'ID': 7,
        'name': 'pineapple',
        'emoji': '🍍',
        'in_stock': 3,
        'price': 3.50
    },
    {
        'ID': 8,
        'name': 'mango',
        'emoji': '🥭',
        'in_stock': 0,
        'price': 3.50
    },
    {
        'ID': 9,
        'name': 'red apple',
        'emoji': '🍎',
        'in_stock': 8,
        'price': 0.50
    },
    {
        'ID': 11,
        'name': 'pear',
        'emoji': '🍐',
        'in_stock': 4,
        'price': 1.00
    },
    {
        'ID': 12,
        'name': 'peach',
        'emoji': '🍑',
        'in_stock': 2,
        'price': 0.75
    },
    {
        'ID': 13,
        'name': 'cherries',
        'emoji': '🍒',
        'in_stock': 20,
        'price': 0.25
    },
    {
        'ID': 14,
        'name': 'strawberry',
        'emoji': '🍓',
        'in_stock': 10,
        'price': 0.25
    },
    {
        'ID': 15,
        'name': 'kiwi',
        'emoji': '🥝',
        'in_stock': 2,
        'price': 1.00
    },
    {
        'ID': 16,
        'name': 'coconut',
        'emoji': '🥥',
        'in_stock': 10,
        'price': 2.50
    }
]


all_food_items = [
    '🍗', '🥩', '🍔', '🍕', '🌭', '🥪', '🌮', '🌯', '🐟'
]

all_side_items = [
    '🥨', '🍟', '🥤'
]

all_dessert_items = [
    '🍦', '🍩', '🍪', '🍰', '🍫'
]
