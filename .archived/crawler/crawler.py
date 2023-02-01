from crawler.driver_wrapper \
    import DriverWrapper

from crawler.lists.history \
    import History

from crawler.lists.temperary.buffer \
    import Buffer

from threading \
    import Thread


class Crawler(Thread):
    def __init__(self):
        super().__init__()

        self.wrapper = DriverWrapper()

        self.buffer = Buffer()
        self.history = History()

        self.debug = True
        self.operational = False

    def setup(self):
        self.set_is_operational( True )

    def insert(
            self,
            href: str
    ) -> None:
        if not (
                self.history.is_in_history(
                    href
                )
        ):
            self.buffer.append(href)

    def load(self) -> None:
        current = self.buffer.current()

        if current is None:
            return

        self.debug_status(current)
        self.history.insert_last_url(current)

        self.wrapper.goto(current)
        self.wrapper.implicit_waiting()

    def is_done(self) -> bool:
        return self.buffer.is_empty()

    def done(self) -> None:
        if self.is_done():
            self.set_is_operational(
                False
            )

            self.wrapper.done()

    def get_debug(self) -> bool:
        return self.debug

    def set_debug(
            self,
            select_value: bool
    ) -> None:
        self.debug = select_value

    def debug_status(
            self,
            url: str
    ) -> None:
        if self.get_debug():
            print("<<<DEBUG::STATUS>>> HERE - " + str(url))

    def is_operational(self) -> bool:
        return self.operational

    def set_is_operational(
            self,
            select_value: bool
    ):
        self.operational = select_value

    def run(self) -> None:
        self.setup()

        while self.is_operational():
            self.load()
            self.done()

