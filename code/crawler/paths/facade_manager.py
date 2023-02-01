from crawler.paths.facade \
    import Facade


def is_facade(facade):
    return issubclass(facade, Facade)


class FacadeManager(object):
    def __init__(self, history, buffer):
        self.facades = []
        self.history = history
        self.buffer = buffer

    def append(self, facade):
        if is_facade(facade):
            print("inserted facade")
            self.facades.append(facade)

    def get_facades(self):
        return self.facades

    def set_facades(self, v):
        self.facades = v

    def size(self):
        return len(self.facades)

    def is_zero(self):
        return self.size() == 0

    def run(self):
        pass

    def update(self):
        pass

    def get_buffer(self):
        return self.buffer

    def set_buffer(self, v):
        self.buffer = v

    def index(self, number) -> Facade:
        return self.facades[number]

