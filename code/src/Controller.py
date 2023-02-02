#!/usr/bin/python
from src.Domain \
    import Domain

from src.actor.Commandline \
    import Commandline


class Controller:
    def __init__(self):
        self.operational = False
        self.commandLine = Commandline()
        self.domain = Domain()

    def initialise(self):
        self.set_operational(True)

    def execute(self):
        while self.is_operational():
            self.commandLine.input()

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

