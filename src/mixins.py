class MixinRepr:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}{tuple(self.__dict__.items())}"
