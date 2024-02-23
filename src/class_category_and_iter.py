from abc import ABC, abstractmethod
from src.class_product_and_descendants import Product


class AbstractCategory(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_products(self, arg):
        pass

    @abstractmethod
    def __len__(self):
        pass


class Category(AbstractCategory):
    """Класс категории товаров"""
    number_of_categories = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1

    @property
    def goods(self):
        list_products = []
        for product in self.__products:
            list_products.append(f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.")
        return list_products

    @property
    def products(self):
        return self.__products

    def add_products(self, product):
        if isinstance(product, Product):
            self.__products.append(product)

    def __len__(self):
        return len(self.__products)

    def __repr__(self):
        return f"Category({self.name}; {self.description}; {self.products})"

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."


class Order(AbstractCategory):
    """Класс заказа"""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.products = []

    def add_products(self, product):
        if self.name == product.name:
            self.price += product.price
            self.quantity += product.quantity
            self.products.append(product)

    def __len__(self):
        return len(self.products)
