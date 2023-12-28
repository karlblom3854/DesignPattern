from framework import Observable, Observer


class User(Observable):
    def __init__(self):
        super().__init__()
        self.__ip = None
        self.__region = None

    def get_login_info(self):
        return [self.__ip, self.__region]

    def login(self, ip, region):
        self.notify_observers([ip, region])
        self.__ip = ip
        self.__region = region


class AbnormalCheck(Observer):
    def update(self, observable, extra_info):
        [last_ip, last_region] = observable.get_login_info()
        if (last_ip is not None and last_region is not None) and (last_ip != extra_info[0] or last_region != extra_info[1]):
            [current_ip, current_region] = extra_info
            print("检查到异常登录！！！")
            print(f"Last IP: {last_ip}, Last Region: {last_region}")
            print(f"Current IP: {current_ip}, Current Region: {current_region}")


if __name__ == '__main__':
    first_user = User()
    checker = AbnormalCheck()

    first_user.add_observer(checker)

    first_user.login('1.1.1.1', 'Local')

    first_user.login('1.1.1.2', 'Local')



