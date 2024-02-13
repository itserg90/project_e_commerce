class Category:
    """Класс категории товаров"""
    number_of_categories = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
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
        self.__products.append(product)

    def __len__(self):
        return len(self.__products)

    def __repr__(self):
        return f"Category({self.name}; {self.description}; {self.products})"

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."


class Product:
    """Класс товара"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, list_products, name, description, price, quantity):
        """Возвращает новый объект товара и проверяет совпадение нового объекта товара с текущим"""
        new_object = cls(name, description, price, quantity)

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
        return self.price * self.quantity + other.price * other.quantity

    def __repr__(self):
        return f"Product({self.name}; {self.description}; {self.price}; {self.quantity})"

    def __str__(self):
        return f"{self.__class__.__name__}, {self.__price} руб. Остаток: {self.quantity} шт."


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
