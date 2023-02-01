
class Counter:
    def __init__(self):
        self.value = 0

    def get_value(self) -> int:
        return self.value

    def set_value(self, v: int):
        self.value = v

    def increase(
            self,
            with_value: int
    ) -> None:
        self.set_value(
            self.get_value() + with_value
        )

    def increment(self) -> None:
        self.increase(1)

    def decrease(
            self,
            with_value: int
    ) -> None:
        self.set_value(
            self.get_value() - with_value
        )

    def decrement(self) -> None:
        self.decrease(1)

    def is_zero(self) -> bool:
        return self.value == 0

    def reset(self) -> None:
        self.set_value(0)

