"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


@pytest.fixture
def smartphone():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(smartphone):
    """Рассчитывает общую стоимость товара Смартфон в магазине."""

    assert smartphone.calculate_total_price() == 200000


def test_apply_discount(smartphone):
    """Вводим скидку 50%, должно вернуть = price * 0.5"""

    Item.pay_rate = 0.5
    smartphone.apply_discount()
    assert smartphone.price == 5000


def test_name(smartphone):
    smartphone.name = "Телефон"
    assert smartphone.name == "Телефон"
    smartphone.name = "Супертелефон"
    assert smartphone.name == "Телефон"
    smartphone.name = "Смартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item_none = Item.instantiate_from_csv('item.csv')
    assert item_none == None


def test_string_to_number():
    assert Item.string_to_number("14") == 14
    assert Item.string_to_number("14.9") == 14
    assert Item.string_to_number("string") == False
    assert Item.string_to_number("") == False


def test_represent():
    item1 = Item("Смартфон", 10000, 20)
    assert Item.__repr__(item1) == "Item('Смартфон', 10000, 20)"


def test_string():
    item_test = Item("Ноутбук", 20000, 10)
    assert Item.__str__(item_test) == "Ноутбук"


def test_add():
    item1 = Item("Телефон", 15000, 5)
    item2 = Item("Монитор", 18000, 3)
    assert item1 + item2 == 8
    assert item1 + 14 == None
