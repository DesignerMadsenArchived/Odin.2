import sys


class CommandlineActor:
    def __init__(self):
        self.default_level = 0
        self.buffer_input = str()

        self.default_prompt = None
        self.reset_default_prompt()

    def get_input(self):
        self.buffer_input = input(
            self.default_prompt
        )

    def empty_buffer(self):
        self.buffer_input = str()

    def send_output(
            self,
            output: str,
            level: int
    ):
        if self.default_level <= level:
            print(output)

    def get_default_level(self) -> int:
        return self.default_level

    def set_default_level(
            self,
            value: int
    ):
        self.default_level = value

    def get_buffer(self) -> str:
        return self.buffer_input

    def set_buffer(
            self,
            with_value: str
    ):
        self.buffer_input = with_value

    def append_to_buffer(
            self,
            with_value: str
    ):
        self.buffer_input = self.buffer_input + with_value

    def get_default_prompt(self) -> str:
        return self.default_prompt

    def set_default_prompt(
            self,
            value: str
    ):
        self.default_prompt = value

    def reset_default_prompt(self):
        self.default_prompt = r'>'

