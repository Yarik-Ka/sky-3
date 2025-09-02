import pytest
from src.product import Product
from src.category import Category

@pytest.fixture
def sample_products():
    return [
        Product("Телефон", "Смартфон", 10000, 5),
        Product("Ноутбук", "Игровой", 50000, 2)
    ]

def test_category_init(sample_products):
    c = Category("Электроника", "Гаджеты", sample_products)
    assert c.name == "Электроника"
    assert c.description == "Гаджеты"
    assert len(c.products) == 2

def test_class_counters(sample_products):
    Category.category_count = 0
    Category.product_count = 0

    Category("Электроника", "Гаджеты", sample_products)
    Category("Одежда", "Мужская", [])

    assert Category.category_count == 2
    assert Category.product_count == 2