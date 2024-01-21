class Singleton2(type):
    def __init__(cls, what, bases=None, dct=None):
        super().__init__(what, bases, dct)
        cls._instance = None  # 初始化全局变量cls._instance为None

    def __call__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__call__(*args)
        return cls._instance


class Customer(metaclass=Singleton2):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    tony = Customer("Tony")
    karry = Customer("Karry")
    print(tony.get_name(), karry.get_name())
    print(f"id(tony): {id(tony)}", f"id(karry): {id(karry)}")
    print("tony == karry", tony == karry)