class Category:
    """Класс категории товаров"""
    number_of_categories = 0
    number_of_products = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        self.number_of_categories += 1
        number = len(set(product.name for product in self.products))
        self.number_of_products += number

    def __repr__(self):
        return f"Category({self.name}; {self.description}; {self.products})"


class Product:
    """Класс товара"""
    name: str
    description: str
    price: float
    count_products: int

    def __init__(self, name, description, price, count_products):
        self.name = name
        self.description = description
        self.price = float(price)
        self.count_products = int(count_products)

    def __repr__(self):
        return f"Product({self.name}; {self.description}; {self.price}; {self.count_products})"
