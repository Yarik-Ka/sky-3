import pytest
from src.product import Product

def test_product_init():
    p = Product("Телефон", "Смартфон", 10000, 5)
    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 10000
    assert p.quantity == 5