#!/usr/bin/python
from selenium \
    import webdriver

from webdriver_manager.chrome \
    import ChromeDriverManager

from selenium.webdriver.chrome.service \
    import Service \
    as ChromeService

from selenium.webdriver.chrome.options \
    import Options \
    as ChromeOptions


class ChromeBrowser:
    def __init__(self):
        self.driver  = None
        self.options = None
        self.service = None

        self.setup()

    def setup(self):
        options = ChromeOptions()

        installation = ChromeDriverManager().install()
        service = ChromeService(installation)

        self.set_options(options)
        self.set_service(service)

        self.set_driver(
            webdriver.Chrome(
                service=self.get_service(),
                options=self.get_options(),
            )
        )

    def get_driver(self) -> webdriver.Chrome:
        return self.driver

    def set_driver(
            self,
            value: webdriver.Chrome
    ):
        self.driver = value

    def get_service(self) -> ChromeService:
        return self.service

    def set_service(
            self,
            service: ChromeService
    ):
        self.service = service

    def get_options(self) -> ChromeOptions:
        return self.options

    def set_options(
            self,
            value: ChromeOptions
    ):
        self.options = value


