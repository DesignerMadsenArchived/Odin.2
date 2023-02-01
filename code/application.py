from domain \
    import Domain

from actors.commandline_actor \
    import CommandlineActor


# https://realpython.com/python-gil/


class Application:
    def __init__(self):
        self.running = True
        self.commandline = CommandlineActor()

        self.domain_area = Domain()
        self.domain_area.set_application(self)

    def initiate(self):
        print("initiate")

    def execute(self):
        while self.get_is_running():
            self.commandline.get_input()

    def cleanup(self):
        print("cleanup")
        self.domain_area.done()

    def flag_exit(self):
        self.set_is_running(
            False
        )

    def get_domain_area(self):
        return self.domain_area

    def set_domains_area(
            self,
            with_domain
    ):
        self.domain_area = with_domain

    def get_is_running(self):
        return self.running

    def set_is_running(
            self,
            with_state
    ):
        self.running = with_state
