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


class HousingAgency:
    """房屋中介"""

    def __init__(self, name):
        self.__house_infos = []
        self.__name = name

    def get_name(self):
        return self.__name

    def add_house_info(self, house_info):
        self.__house_infos.append(house_info)

    def remove_house_info(self, house_info):
        for info in self.__house_infos:
            if house_info == info:
                self.__house_infos.remove(info)

    def get_search_condition(self, description):
        """将用户描述信息转为搜索条件"""
        return description

    def get_match_infos(self, search_condition):
        print(f"{self.get_name()}为您找到以下合适的房源：")
        for info in self.__house_infos:
            info.show_info()

        return self.__house_infos

    def sign_contract(self, house_info, period):
        print(self.get_name(), "与房东", house_info.get_owner_name(), "签订", house_info.get_address(),
              "的房子的租赁合同，租期", period, "年。合同期内", self.get_name(), "有权对其进行使用和转租！")

    def sign_contracts(self, period):
        for info in self.__house_infos:
            self.sign_contract(info, period)


class HouseOwner:
    """房东"""
    def __init__(self, name):
        self.__name = name
        self.__house_info = None

    def get_name(self):
        return self.__name

    def set_house_info(self, address, area, price, has_window, bathroom, kitchen):
        self.__house_info = HouseInfo(area, price, has_window, bathroom, kitchen, address, self.get_name())

    def publish_house_info(self, agency):
        agency.add_house_info(self.__house_info)
        print(f"{self.get_name()}在{agency.get_name()}发布房源信息：")
        self.__house_info.show_info()


class Customer:
    """租户"""
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def find_house(self, description, agency):
        print(f"我是{self.get_name()}，我想找一个{description}的房子")
        return agency.get_match_infos(agency.get_search_condition(description))

    def see_house(self, house_infos):
        size = len(house_infos)
        return house_infos[size-1]

    def sign_contract(self, agency, house_info, period):
        print(f"{self.get_name()}，与中介{agency.get_name()}签订{house_info.get_address()}的房子的租赁合同，"
              f"租期{period}年，合同期内，{self.get_name()}，有权对其进行使用！")


if __name__ == '__main__':
    my_home = HousingAgency("我爱我家")
    carl = HouseOwner("Carl")
    carl.set_house_info("上地1", "20", "2500", 1, "独立卫生间", 0)
    carl.publish_house_info(my_home)

    smith = HouseOwner("Smith")
    smith.set_house_info("上地2", "25", "2750", 1, "独立卫生间", 0)
    smith.publish_house_info(my_home)

    bob = HouseOwner("Bob")
    bob.set_house_info("上地3", "30", "3000", 1, "独立卫生间", 0)
    bob.publish_house_info(my_home)
    print()

    my_home.sign_contracts(3)
    print()

    tony = Customer("Tony")
    house_infos = tony.find_house("上地，18平方米左右", my_home)
    print()

    appropriate_house = tony.see_house(house_infos)

    tony.sign_contract(my_home, appropriate_house, 1)
