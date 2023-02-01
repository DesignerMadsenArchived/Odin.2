from crawler.crawler \
    import Crawler

from loader \
    import Loader

import threading


class Domain:
    def __init__(self):
        self.application = None
        self.__thread_call = None

        self.crawler = None

        self.set_crawler(
            Crawler()
        )

        self.loader = Loader(
            self.get_crawler()
        )

        self.first_time = False

        self.loader.load()

    def operate(self) -> None:
        if not self.first_time:
            self.first_time = True
            self.process_start()

    def process_start(self) -> None:
        if not self.crawler.is_operational():
            self.__thread_call = threading.Thread(
                target=self.crawler
            )

    def done(self) -> None:
        pass

    def set_application(
            self,
            with_value
    ) -> None:
        self.application = with_value

    def get_application(self):
        return self.application

    def get_crawler(self):
        return self.crawler

    def set_crawler(
            self,
            with_value: Crawler
    ) -> None:
        self.crawler = with_value
