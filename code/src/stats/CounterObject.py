
class CounterObject:
    def __init__(self):
        self.current_position = 0

    def get_position(self) -> int:
        return self.current_position

    def set_position(self, value: int):
        self.current_position = value

    def increase(self, value: int):
        self.set_position(self.get_position() + value)

    def decrease(self, value: int):
        self.set_position(self.get_position() - value)

    def decrement(self):
        self.decrease(1)

    def increment(self):
        self.increase(1)

