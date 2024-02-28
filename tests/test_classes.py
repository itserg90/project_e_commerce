import pytest

from src import utils
from src.class_category_and_iter import IterationProducts
from src.class_product_and_descendants import Product, Smartphone
from src.my_exceptions import MyExceptionZeroQuantity


def test_init_category(category_phones):
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Phones"
    assert category_phones.products[0].name == "Iphone 15"


def test_init_product(product_phones_iphone15):
    assert product_phones_iphone15.name == "Iphone 15"
    assert product_phones_iphone15.description == "512GB, Gray space"
    assert product_phones_iphone15.price == 215_000.00
    assert product_phones_iphone15.quantity == 8


def test_number_of_categories(category_phones):
    assert category_phones.number_of_categories == 2


def test_len_of_products_in_category(category_phones):
    assert len(category_phones) == 1


def test_load_json():
    assert utils.load_json("https://www.jsonkeeper.com/b/F7TP")[0]["name"] == "Смартфоны"


def test_convert_json(dict_category_and_products):
    current_category = [dict_category_and_products]
    assert utils.convert_json(current_category)[0].name == "Смартфоны"


def test_goods_in_category(category_phones):
    assert category_phones.goods == ['Iphone 15, 210000 руб. Остаток: 8 шт.']


def test_new_product(product_phones_iphone15, product_class_smartphone):
    new_product_product = Product.new_product(product_phones_iphone15.name,
                                              product_phones_iphone15.description,
                                              product_phones_iphone15.price,
                                              product_phones_iphone15.quantity,
                                              product_phones_iphone15.color)
    assert new_product_product.name == "Iphone 15"

    new_product_smartphone = Smartphone.new_product(product_class_smartphone.name,
                                                    product_class_smartphone.description,
                                                    product_class_smartphone.price,
                                                    product_class_smartphone.quantity,
                                                    product_class_smartphone.color,
                                                    product_class_smartphone.performance,
                                                    product_class_smartphone.model,
                                                    product_class_smartphone.memory)
    assert new_product_smartphone.model == "15"


def test_check_new_product(category_phones, product_phones_iphone15, category_lawn_grass, product_class_lawn_grass):
    product_phones_iphone15.check_new_product(category_phones.products)
    assert category_phones.products[0].quantity == 16
    assert category_phones.products[0].price == 215_000.0

    product_class_lawn_grass.check_new_product(category_lawn_grass.products)
    assert category_lawn_grass.products[0].quantity == 16
    assert category_lawn_grass.products[0].price == 100_000.0


def test_add_products_in_category(category_phones, product_phones_iphone14):
    category_phones.add_products(product_phones_iphone14)
    assert category_phones.products[1].name == "Iphone 14"
    assert len(category_phones.products) == 2
    category_phones.add_products(1)
    assert len(category_phones.products) == 2


def test_add_products_in_category_with_raises(category_phones, order1, product_phones_iphone15):
    product_phones_iphone15.quantity = 0
    with pytest.raises(MyExceptionZeroQuantity):
        category_phones.add_products(product_phones_iphone15)
    with pytest.raises(MyExceptionZeroQuantity):
        order1.add_products(product_phones_iphone15)


def test_price_in_product(category_phones):
    category_phones.products[0].price = 215_000.0
    assert category_phones.products[0].price == 215_000.0


def test_add_in_product_product(product_phones_iphone15, product_class_smartphone, product_class_lawn_grass):
    total = product_phones_iphone15 + product_phones_iphone15
    assert total == 3_440_000.0


def test_add_in_product_number(product_phones_iphone15):
    with pytest.raises(TypeError):
        product_phones_iphone15.__add__(1)


def test_add_in_smartphone_lawn_grass(product_class_smartphone, product_class_lawn_grass):
    with pytest.raises(TypeError):
        product_class_smartphone.__add__(product_class_lawn_grass)


def test_add_in_smartphone_product(product_phones_iphone15, product_class_smartphone):
    with pytest.raises(TypeError):
        product_class_smartphone.__add__(product_phones_iphone15)


def test_add_in_lawn_grass_product(product_phones_iphone15, product_class_lawn_grass):
    with pytest.raises(TypeError):
        product_class_lawn_grass.__add__(product_phones_iphone15)


def test_add_in_product_zero(product_phones_iphone15):
    with pytest.raises(TypeError):
        product_phones_iphone15.__add__(0)


def test_iteration_products_in_category(dict_category_phones):
    list_of_product = []
    for product in IterationProducts(dict_category_phones):
        list_of_product.append(product)
    assert len(list_of_product) == 1


def test_product_class_smartphone(product_class_smartphone):
    assert product_class_smartphone.name == "Iphone 15"
    assert product_class_smartphone.color == "white"


def test_product_class_lawn_grass(product_class_lawn_grass):
    assert product_class_lawn_grass.name == "Lawn"
    assert product_class_lawn_grass.color == "green"


def test_calculate_the_average_price(category_phones, product_phones_iphone14):
    category_phones.add_products(product_phones_iphone14)
    assert category_phones.calculate_the_average_price() == 212_500.0


def test_calculate_the_average_price_division_by_zero(category_phones):
    del category_phones.products[0]
    assert category_phones.calculate_the_average_price() == 0
