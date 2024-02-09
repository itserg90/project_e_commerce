from src import utils
from src import classes


def test_init_category(category_phones):
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Phones"
    assert category_phones.products[0].name == "Iphone 15"


def test_init_product(product_phones):
    assert product_phones.name == "Iphone 15"
    assert product_phones.description == "512GB, Gray space"
    assert product_phones.price == 215_000.00
    assert product_phones.quantity == 8


def test_number_of_categories(category_phones):
    assert category_phones.number_of_categories == 2


def test_number_of_products(category_phones):
    assert category_phones.number_of_products == 1


def test_load_json():
    assert utils.load_json("https://www.jsonkeeper.com/b/F7TP")[0]["name"] == "Смартфоны"


def test_convert_json():
    current_category = [{"name": "Смартфоны",
                         "description": "Iphones",
                         "products": [{"name": "Iphone 15",
                                       "description": "512BGB",
                                       "price": 210_000.0,
                                       "quantity": 8}]}]
    assert utils.convert_json(current_category)[0].name == "Смартфоны"


def test_goods(category_phones):
    assert category_phones.goods == ['Iphone 15, 210000 руб. Остаток: 8 шт.']


def test_new_product(product_phones):
    current_category = classes.Category("Смартфоны",
                                        "Iphones",
                                        [classes.Product("Iphone 15",
                                                         "512GB",
                                                         210_000.0,
                                                         8)])
    classes.Product.new_product(current_category.products[0],
                                product_phones.name,
                                product_phones.description,
                                product_phones.price,
                                product_phones.quantity)
    assert current_category.products[0].quantity == 16
    assert current_category.products[0].price == 215_000.0


def test_products(product_phones):
    current_category = classes.Category("Смартфоны",
                                        "Iphones",
                                        [classes.Product("Iphone 14",
                                                         "512GB",
                                                         210_000.0,
                                                         8)])
    current_category.add_products(product_phones)
    assert current_category.products[1].name == "Iphone 15"


def test_price():
    current_category = classes.Category("Смартфоны",
                                        "Iphones",
                                        [classes.Product("Iphone 15",
                                                         "512GB",
                                                         210_000.0,
                                                         8)])
    current_category.products[0].price = 215_000.0
    assert current_category.products[0].price == 215_000.0
