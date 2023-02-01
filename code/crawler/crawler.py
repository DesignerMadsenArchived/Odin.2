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

    def setup(self):
        pass

    def insert(
            self,
            href
    ):
        if not (
                self.history.is_in_history(
                    href
                )
        ):
            self.buffer.append(href)

    def load(self):
        current = self.buffer.current()

        self.debug_status(current)
        self.history.insert_last_url(current)

        self.wrapper.goto(current)
        self.wrapper.sleep()

    def is_done(self):
        return self.buffer.is_empty()

    def done(self):
        self.wrapper.done()

    def debug_status(self, url):
        print("==> here " + str(url))