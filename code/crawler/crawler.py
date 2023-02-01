from crawler.driver_wrapper \
    import DriverWrapper

from crawler.lists.history \
    import History

from crawler.lists.temperary.buffer \
    import Buffer


class Crawler:
    def __init__(self):
        self.wrapper = DriverWrapper()

        self.buffer = Buffer()
        self.history = History()
        self.debug = True

    def setup(self):
        pass

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

        self.debug_status(current)
        self.history.insert_last_url(current)

        self.wrapper.goto(current)
        self.wrapper.sleep()

    def is_done(self) -> bool:
        return self.buffer.is_empty()

    def done(self) -> None:
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