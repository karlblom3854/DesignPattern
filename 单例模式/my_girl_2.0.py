from framework import singleton_decorator


@singleton_decorator
class MyGirl:
    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print(f"{name} is my only!")
        else:
            print(f"{name} is not my only!")

    def show_info(self):
        print(f"So, {self.__name} is my only!")


if __name__ == '__main__':
    tony = MyGirl("Tony")
    tony.show_info()

    kimi = MyGirl("Kimi")
    kimi.show_info()

    print(f"id(Tony):{id(tony)}\tid(Kimi):{id(kimi)}")

