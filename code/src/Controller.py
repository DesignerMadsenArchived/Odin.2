from src.Domain \
    import Domain


class Controller:
    def __init__(self):
        self.operational = False

    def initialise(self):
        pass

    def execute(self):
        while self.is_operational():
            pass

    def cleanup(self):
        pass

    def is_operational(self) -> bool:
        return self.operational

    def set_operational(
            self,
            value: bool
    ):
        self.operational = value

    def flag_exit(self):
        self.set_operational(False)

