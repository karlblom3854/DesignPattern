class MyGirl(object):
    __instance = None
    __is_first_init = False

    def __new__(cls, name):
        if not cls.__instance:
            MyGirl.__instance = super().__new__(cls)
        return cls.__instance  # ?

    def __init__(self, name):
        if not self.__is_first_init:
            self.__name = name
            print(f"{name} is my only!")
            self.__is_first_init = True
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
