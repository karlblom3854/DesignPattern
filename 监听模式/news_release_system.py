# 假设你正在开发一个简单的新闻发布系统，当有新的新闻发布时，你希望能够通知多个订阅者（观察者）。
# 请设计一个使用观察者模式的新闻发布系统。
# 以下是问题的一些建议要点：
# 定义观察者接口： 创建一个Observer接口，其中包含一个update方法，用于在新闻发布时通知观察者。
# 实现具体观察者类： 创建两个或更多的具体观察者类，例如SubscriberA和SubscriberB，
#                 它们实现了Observer接口，并在update方法中定义了接收新闻通知的行为。
# 定义主题（Subject）类： 创建一个主题类，例如NewsPublisher，
#                      它维护一个观察者列表，并包含用于添加、删除和通知观察者的方法。
# 测试： 编写一个测试脚本，创建一个发布者和多个订阅者，并演示如何发布新闻时通知所有订阅者。
from framework import Observable, Observer


class NewsPublisher(Observable):
    def __init__(self):
        super().__init__()
        self.__subscribers = []
        self.__news = {}

    def publish_news(self, news):
        self.__news = news
        self.notify_observers(news)

    def add_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.remove_subscriber(subscriber)


class SubscriberA(Observer):
    def update(self, observable, message):
        print("===订阅者A收到通知===")
        print(f"\t收到新发布的新闻消息\tTitle：{message['Title']}\n")


class SubscriberB(Observer):
    def update(self, observable, message):
        print("===订阅者B收到通知===")
        print(f"\t收到新发布的新闻消息\tTitle：{message['Title']}\n")


if __name__ == '__main__':
    publisher = NewsPublisher()

    subscriber_A = SubscriberA()
    subscriber_B = SubscriberB()

    publisher.add_observer(subscriber_A)
    publisher.add_observer(subscriber_B)

    publisher.publish_news({"Title": "lay cheated!"})
