import pytest
from src.product import Product

def test_product_init():
    p = Product("Телефон", "Смартфон", 10000, 5)
    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 10000
    assert p.quantity == 5

def test_price_setter_positive():
    p = Product("Телефон", "Смартфон", 10000, 5)
    p.price = 15000
    assert p.price == 15000

def test_price_setter_negative(capsys):
    p = Product("Телефон", "Смартфон", 10000, 5)
    p.price = -500
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 10000

def test_new_product():
    data = {
        "name": "Планшет",
        "description": "Удобный планшет",
        "price": 20000,
        "quantity": 3
    }
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Планшет"