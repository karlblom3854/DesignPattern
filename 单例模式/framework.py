
def singleton_decorator(cls, *args, **kwargs):
    instances = {}

    def wrapper_singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper_singleton


@singleton_decorator
class Singleton3:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    tony = Singleton3("Tony")
    karry = Singleton3("Karry")

    print(tony.get_name(), karry.get_name())
    print(f"id(tony): {id(tony)}, id(karry): {id(karry)}")
    print(f"tony == karry: {tony == karry}")
