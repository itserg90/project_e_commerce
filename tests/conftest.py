import pytest

from src import classes


@pytest.fixture()
def category_phones():
    return classes.Category("Смартфоны",
                            "Phones",
                            [classes.Product("Iphone 15", "512GB, Gray space", 210_000.0, 8, "white")])


@pytest.fixture()
def product_phones_iphone14():
    return classes.Product("Iphone 14", "512GB, Gray space", 215_000.0, 8, "white")


@pytest.fixture()
def product_phones_iphone15():
    return classes.Product("Iphone 15", "512GB, Gray space", 215_000.0, 8, "white")


@pytest.fixture()
def dict_category_phones():
    return {"name": "Смартфоны",
            "description": "Phones",
            "products": [classes.Product("Iphone 15", "512GB, Gray space", 210_000.0, 8, "white")]}


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
    return classes.Smartphone("Iphone 15", "512GB, Gray space", 215_000.0, 8, "white", "8GB", "15", "512GB")


@pytest.fixture()
def product_class_lawn_grass():
    return classes.LawnGrass("Lawn", "Lawn Grass", 100_000, 8, "green", "Russia", "2 weeks")
