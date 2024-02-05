from framework import ProxySubject, RealSubject


class RealDownloader(RealSubject):
    def __init__(self, name, url):
        super().__init__(name)
        self.__url = url

    def request(self, content):
        print(f"正在下载{self.__url}...")


class ProxyDownloader(ProxySubject):
    def __init__(self, name, url):
        super().__init__(name, url)

    def pre_process(self):
        print(f"代理下载开始...")

    def post_process(self):
        print(f"代理下载结束！！！")


if __name__ == '__main__':
    web = "https://example.com/sample.pdf"
    real_downloader = RealDownloader("Read Downloader", web)
    proxy_downloader = ProxyDownloader("Proxy Downloader", real_downloader)
    # 使用代理下载文件
    proxy_downloader.request(None)

