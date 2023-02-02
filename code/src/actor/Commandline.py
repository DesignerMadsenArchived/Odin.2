class Commandline:
    def __init__(self):
        self.buffer = str()

    def input(self):
        v = input(' >> ')
        self.append(v)

    def get_buffer(self):
        return self.buffer

    def set_buffer(
            self,
            value: str
    ):
        self.buffer = value

    def append(
            self,
            value: str
    ):
        self.set_buffer(
            self.get_buffer() + value
        )

    def reset(self):
        self.set_buffer(str())

