import requests

from src import classes

# JSON в облачном хранилище
path_name = "https://www.jsonkeeper.com/b/F7TP"


def load_json(filename: str) -> list:
    """Подгружает файл формата JSON"""
    return requests.get(filename).json()


def convert_json(categories: list) -> list:
    """Возвращает список обьектов классов Category и Product"""

    list_of_categories = []
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


# # Проверка
# categories_in_list = load_json(path_name)
#
# # на изменение цены
# for obj in convert_json(categories_in_list):
#     for prod in obj.products:
#         print(prod.price)
#         user_price = float(input())
#         prod.price = user_price
#     print(obj)
#
# # на добавление нового объекта товара
# for obj in convert_json(categories_in_list):
#     flag = False
#     name_cat, name, description, price, quantity = "Смартфоны", "Iphone 15", "512GB, Gray space", 220_000, 8
#     if obj.name == name_cat:
#         for prod in obj.products:
#             if name == prod.name:
#                 prod.new_product(name, description, price, quantity)
#                 flag = True
#                 break
#         if not flag:
#             obj.products.append(classes.Product(name, description, price, quantity))
#     print(obj)
