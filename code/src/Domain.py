#!/usr/bin/python
from threading \
    import Thread

from src.crawler.Crawler \
    import Crawler


class Domain:
    def __init__(self):
        self.crawler = Crawler()

        self.thread = Thread(
            target=self.crawler.run()
        )

        self.thread.start()

    def get_crawler(self) -> Crawler:
        return self.crawler

    def set_crawler(
            self,
            value: Crawler
    ):
        self.crawler = value