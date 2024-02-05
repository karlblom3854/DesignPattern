from framework import RealSubject, ProxySubject


class TonyReception(RealSubject):
    def __init__(self, name, phone_num):
        super().__init__(name)
        self.__phone_num = phone_num

    def get_phone(self):
        return self.__phone_num

    def request(self, content):
        print(f"姓名：{self.get_name()}\t联系电话：{self.get_phone()}")
        print(f"包裹：{content}")


class WendyReception(ProxySubject):
    def __init__(self, name, subject):
        super().__init__(name, subject)

    def pre_process(self):
        print(f"我是{self._subject.get_name()}的朋友{self.get_name()}，我来帮他取快递！")

    def post_process(self):
        print(f"代取人：{self._subject.get_name()}")


if __name__ == '__main__':
    tony = TonyReception("Tony", "0101010101")
    print(f"Tony接收：")
    tony.request("MacBook")
    print()

    print(f"Wendy代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.request("iWatch")
