from application \
    import Application

from crawler.crawler \
    import Crawler

from loader \
    import Loader


class Domain:
    def __init__(self):
        self.application = None

        self.crawler = Crawler()

        self.loader = Loader(
            self.get_crawler()
        )

        self.loader.load()

    def operate(self):
        if not self.crawler.is_done():
            self.process()
        else:
            self.application.flag_exit()

    def process(self):
        self.crawler.load()

    def done(self):
        self.crawler.done()

    def set_application(
            self,
            with_value: Application
    ):
        self.application = with_value

    def get_application(self) -> Application:
        return self.application

    def get_crawler(self):
        return self.crawler

    def set_crawler(
            self,
            with_value: Crawler
    ):
        self.crawler = with_value
