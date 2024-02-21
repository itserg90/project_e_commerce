class Product:
    """Класс товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @classmethod
    def new_product(cls, list_products, name, description, price, quantity, color):
        """Возвращает новый объект товара и проверяет совпадение нового объекта товара с текущим"""
        new_object = cls(name, description, price, quantity, color)

        for product in list_products:
            if product.name == new_object.name:
                product.quantity += new_object.quantity
                if new_object.price > product.price:
                    product.price = new_object.price
        return new_object

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

    def __repr__(self):
        return f"Product({self.name}; {self.description}; {self.price}; {self.quantity})"

    def __str__(self):
        return f"{self.__class__.__name__}, {self.__price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 color: str, performance: str, model: str, memory: str):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 color: str, country: str, germination_period: str):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
