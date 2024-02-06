import requests

from src import classes

# JSON в облачном хранилище
path_name = "https://www.jsonkeeper.com/b/F7TP"


def load_json(filename: str) -> list:
    """Подгружает файл формата JSON и возвращает список обьектов классов Category и Product"""

    list_of_categories = []
    categories = requests.get(filename).json()
    for category in categories:
        list_of_products = []
        for product in category["products"]:
            object_product = classes.Product(product["name"],
                                             product["description"],
                                             product["price"],
                                             product["quantity"])
            list_of_products.append(object_product)
        object_category = classes.Category(category["name"],
                                           category["description"],
                                           list_of_products)
        list_of_categories.append(object_category)

    return list_of_categories
