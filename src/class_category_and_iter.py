from src.class_product_and_descendants import Product


class Category:
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
