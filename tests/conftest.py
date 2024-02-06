import pytest

from src import classes


@pytest.fixture()
def category_phones():
    return classes.Category("Phones",
                            "Phones are smart",
                            [classes.Product("Samsung", "Samsung Galaxy C23 Ultra", 50000.0, 2)])


@pytest.fixture()
def product_phones():
    return classes.Product("Samsung", "Samsung Galaxy C23 Ultra", 50000.0, 2)
