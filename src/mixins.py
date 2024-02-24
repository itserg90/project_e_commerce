class MixinRepr:
    def __init__(self):
        print(MixinRepr.__repr__(self))

    def __repr__(self):
        return f"{self.__class__.__name__}{tuple(self.__dict__.items())}"
