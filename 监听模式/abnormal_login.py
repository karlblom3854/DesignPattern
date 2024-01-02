import time

from framework import Observable, Observer


def get_region(ip):
    ip_regions = {
        "101.47.18.9": "浙江省杭州市",
        "67.218.147.69": "美国洛杉矶"
    }
    region = ip_regions.get(ip)
    return "" if region is None else region


class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__last_ip = []
        self.__last_region = []

    def login(self, ip):
        region = get_region(ip)
        if self.__is_long_dist(region):
            self.notify_observers({"ip": ip, "region": region})
        self.__last_ip = None
        self.__last_region = None

    # ---functional function--- #
    def __is_long_dist(self, region):
        last_region = self.__last_region
        return last_region is not None and last_region != region


class SmsSender(Observer):
    def update(self, observable, info):
        print("***短信***")
        print("\t检查到异常登录情况，最近一次登录信息：")
        print(f"\t登录时间：{time.time()}，"
              f"登录IP：{info['ip']}，登录位置：{info['region']}\n")


class MailSender(Observer):
    def update(self, observable, info):
        print("***邮件***")
        print("\t检查到异常登录情况，最近一次登录信息：")
        print(f"\t登录时间：{time.time()}，"
              f"登录IP：{info['ip']}，登录位置：{info['region']}\n")


if __name__ == '__main__':
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(MailSender())

    account.login('101.47.18.9')
    account.login('67.218.147.69')
