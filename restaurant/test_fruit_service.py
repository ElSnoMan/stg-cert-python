from restaurant import fruit_service


def test_get_all_fruits():
    fruits = fruit_service.get_all_fruits()
    assert len(fruits) == 16


def test_get_fruit_by_name():
    fruit = fruit_service.get_fruit_by_name('cherry')
    assert fruit['name'] == 'cherry'


def test_get_fruits_by_price():
    fruits = fruit_service.get_fruits_by_price(1.00)
    for fruit in fruits:
        assert fruit['price'] == 1.00


def test_purchasing_fruit():
    assert fruit_service.get_fruit_by_name('banana')['in_stock'] == 12
    response = fruit_service.purchase_fruit('banana', 10)
    assert 'Success' in response
    assert fruit_service.get_fruit_by_name('banana')['in_stock'] == 2
