class MyExceptionZeroQuantity(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else "Количество товаров ноль, товар не добавлен"

    def __str__(self):
        return self.message
