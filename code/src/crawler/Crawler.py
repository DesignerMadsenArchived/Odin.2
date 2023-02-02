#!/usr/bin/python
from src.crawler.browser.ChromeBrowser \
    import ChromeBrowser

from threading \
    import Thread

import time


class Crawler(Thread):
    def __init__(self):
        super().__init__()
        self.browser = None
        self.ttw = 1
        self.operational = False

    def run(self) -> None:
        while self.is_operational():
            time.sleep(
                self.get_ttw()
            )

    def get_browser(self) -> ChromeBrowser:
        return self.browser

    def set_browser(
            self,
            value: ChromeBrowser
    ):
        self.browser = value

    def get_ttw(self) -> int:
        return self.ttw

    def set_ttw(
            self,
            ttw: int
    ):
        self.ttw = ttw

    def is_operational(self) -> bool:
        return self.operational

    def set_operational(
            self,
            value: bool
    ):
        self.operational = value

