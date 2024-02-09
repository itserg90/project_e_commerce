import pytest

from src import classes


@pytest.fixture()
def category_phones():
    return classes.Category("Смартфоны",
                            "Phones",
                            [classes.Product("Iphone 15", "512GB, Gray space", 210_000.0, 8)])


@pytest.fixture()
def product_phones():
    return classes.Product("Iphone 15", "512GB, Gray space", 215_000.0, 8)
