from abc import ABC, abstractmethod
from src.class_product_and_descendants import Product
from src.my_exceptions import MyExceptionZeroQuantity


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

    @staticmethod
    def check_product(product):
        if not product.quantity:
            raise MyExceptionZeroQuantity()

    def add_products(self, product):
        if isinstance(product, Product):
            try:
                self.check_product(product)
                self.__products.append(product)
            except MyExceptionZeroQuantity as error:
                print(error)
            else:
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")

    def calculate_the_average_price(self):
        total = sum(product.price for product in self.products)
        try:
            return round(total / len(self), 1)
        except ZeroDivisionError:
            return 0

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

    @staticmethod
    def check_product(product):
        if product.quantity == 0:
            raise MyExceptionZeroQuantity()

    def add_products(self, product):
        if not self.name == product.name:
            try:
                self.check_product(product)
                self.price += product.price
                self.quantity += product.quantity
                self.products.append(product)
            except MyExceptionZeroQuantity as error:
                print(error)
            else:
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")

    def __len__(self):
        return len(self.products)


class IterationProducts:
    def __init__(self, category):
        self.category = category["products"]

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < len(self.category):
            self.current_value += 1
            return self.category[self.current_value]
        else:
            raise StopIteration


# if __name__ == "__main__":
#     category1 = Category("Sm",
#                          "ssmm",
#                          [Product("sm1", "ssmm1", 100, 2, "white")])
#     order1 = Order("Iphone16", 300_000, 2)
#
#     category1.add_products(Product("sm1", "ssmm1", 100, 1, "white"))
#     order1.add_products(Product("sm1", "ssmm1", 100, 0, "white"))
