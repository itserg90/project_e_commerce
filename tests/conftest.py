import pytest

from src.class_category_and_iter import Category
from src.class_product_and_descendants import Product, Smartphone, LawnGrass


@pytest.fixture()
def category_phones():
    return Category("Смартфоны",
                    "Phones",
                    [Product("Iphone 15", "512GB, Gray space", 210_000.0, 8, "white")])


@pytest.fixture()
def product_phones_iphone14():
    return Product("Iphone 14", "512GB, Gray space", 215_000.0, 8, "white")


@pytest.fixture()
def product_phones_iphone15():
    return Product("Iphone 15", "512GB, Gray space", 215_000.0, 8, "white")


@pytest.fixture()
def dict_category_phones():
    return {"name": "Смартфоны",
            "description": "Phones",
            "products": [Product("Iphone 15", "512GB, Gray space", 210_000.0, 8, "white")]}


@pytest.fixture()
def dict_category_and_products():
    return {"name": "Смартфоны",
            "description": "Phones",
            "products": [{"name": "Iphone 15",
                          "description": "512GB, Gray space",
                          "price": 210_000.0,
                          "quantity": 8,
                          "color": "white"}]}


@pytest.fixture()
def product_class_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 215_000.0, 8, "white", "8GB", "15", "512GB")


@pytest.fixture()
def category_lawn_grass():
    return Category("Lawns",
                    "All types",
                    [LawnGrass("Lawn", "Lawn Grass", 90_000, 8, "green", "Russia", "2 weeks")])


@pytest.fixture()
def product_class_lawn_grass():
    return LawnGrass("Lawn", "Lawn Grass", 100_000, 8, "green", "Russia", "2 weeks")
