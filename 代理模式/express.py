from abc import ABCMeta, abstractmethod


class ReceiveParcel(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def receive(self, parcel_content):
        pass


class TonyReception(ReceiveParcel):
    def __init__(self, name, phone_num):
        super().__init__(name)
        self.__phone_num = phone_num

    def get_phone(self):
        return self.__phone_num

    def receive(self, parcel_content):
        print(f"姓名：{self.get_name()}\t联系电话：{self.get_phone()}")
        print(f"包裹：{parcel_content}")


class WendyReception(ReceiveParcel):
    def __init__(self, name, receiver):
        super().__init__(name)
        self.__receiver = receiver

    def receive(self, parcel_content):
        print(f"我是{self.__receiver.get_name()}的代理人，我来帮他取快递！")
        if self.__receiver is not None:
            self.__receiver.receive(parcel_content)
        print(f"代收人：{self.get_name()}")


if __name__ == '__main__':
    tony = TonyReception("Tony", "1**1234****")
    print(f"Tony接收：")
    tony.receive("MacBook")
    print()

    print(f"Wendy代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.receive("iWatch")