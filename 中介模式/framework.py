class HouseInfo:
    """房源信息"""
    def __init__(self, area, price, has_window, has_bathroom, has_kitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__has_window = has_window
        self.__has_bathroom = has_bathroom
        self.__has_kitchen = has_kitchen
        self.__address = address
        self.__owner = owner

    def get_address(self):
        return self.__address

    def get_owner_name(self):
        return self.__owner

    def show_info(self):
        print(f"面积：{self.__area}平方米，价格：{self.__price}，" +
              f"窗户：" + ("有" if self.__has_window else "没有") +
              "卫生间：" + ("有" if self.__has_bathroom else "没有") +
              "厨房：" + ("有" if self.__has_kitchen else "没有") +
              f"地址：{self.__address}，房东：{self.__owner}")
