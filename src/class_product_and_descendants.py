from abc import ABC, abstractmethod

from src.mixins import MixinRepr


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args):
        pass

    @abstractmethod
    def check_new_product(self, arg):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, arg):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Product(MixinRepr, AbstractProduct):
    """Класс товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @classmethod
    def new_product(cls, *args):
        """Возвращает новый объект товара"""
        return cls(*args)

    def check_new_product(self, list_products):
        """Проверяет совпадение нового объекта товара с текущим"""
        for product in list_products:
            if product.name == self.name:
                product.quantity += self.quantity
                if self.price > product.price:
                    product.price = self.price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > self.__price:
            self.__price = price
        elif price < 0 or price == self.__price:
            print("Цена введена некорректно")
        else:
            while True:
                user_answer = input("Цена понизилась. Установить эту цену?(y-да, n-нет)")
                if user_answer == "y":
                    self.__price = price
                    break
                elif user_answer == "n":
                    print("Цена осталась прежней.")
                    break
                else:
                    print("Пожалуйста, введите корректный ответ: y или n(y-да, n-нет)")

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    def __str__(self):
        return f"{self.__class__.__name__}, {self.__price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    """Класс товара"""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 color: str, performance: str, model: str, memory: str):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    """Класс товара"""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 color: str, country: str, germination_period: str):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
