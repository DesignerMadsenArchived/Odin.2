
class Counter:
    def __init__(self):
        self.value = 0

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v

    def increase(
            self,
            with_value
    ):
        self.set_value(
            self.get_value() + with_value
        )

    def increment(self):
        self.increase(1)

    def decrease(
            self,
            with_value
    ):
        self.set_value(
            self.get_value() - with_value
        )

    def decrement(self):
        self.decrease(1)

    def is_zero(self):
        return self.value == 0
