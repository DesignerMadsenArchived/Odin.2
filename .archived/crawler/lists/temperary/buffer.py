class Buffer:
    def __init__(self):
        self.list = []

    def get_buffer(self):
        return self.list

    def set_buffer(
            self,
            with_set
    ):
        self.list = with_set

    def current(self):
        if self.is_empty():
            return None

        current = self.list[
            self.__begin_at_position()
        ]

        self.list.pop(
            self.__begin_at_position()
        )

        return current

    def append(self, href):
        array_buffer = self.get_buffer()
        array_buffer.append(href)

    def size(self):
        return len(self.list)

    def is_empty(self):
        return self.size() == 0

    def __begin_at_position(self) -> int:
        return 0


