from src import classes, utils


def test_init_category(category_phones):
    assert category_phones.name == "Phones"
    assert category_phones.description == "Phones are smart"
    assert category_phones.products[0].name == "Samsung"


def test_init_product(product_phones):
    assert product_phones.name == "Samsung"
    assert product_phones.description == "Samsung Galaxy C23 Ultra"
    assert product_phones.price == 50_000.00
    assert product_phones.count_products == 2


def test_number_of_categories(category_phones):
    assert category_phones.number_of_categories == 1


def test_number_of_products(category_phones):
    assert category_phones.number_of_products == 1


def test_json():
    assert utils.load_json("https://www.jsonkeeper.com/b/F7TP")[0].name == "Смартфоны"
