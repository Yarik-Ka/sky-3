import pytest
from src.product import Product

def test_str_product():
    p = Product("Телефон", "Смартфон", 10000, 5)
    assert str(p) == "Телефон, 10000 руб. Остаток: 5 шт."

def test_add_products():
    p1 = Product("Телефон", "Смартфон", 10000, 5)  # 50 000
    p2 = Product("Ноутбук", "Игровой", 50000, 2)   # 100 000
    assert p1 + p2 == 150000