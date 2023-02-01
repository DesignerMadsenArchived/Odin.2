from src.Controller \
    import Controller


class Application:
    def __init__(self):
        self.controller = Controller()

    def execute_stages(self):
        self.get_controller().initialise()
        self.get_controller().execute()
        self.get_controller().cleanup()

    def set_controller(
            self,
            value: Controller
    ):
        self.controller = value

    def get_controller(self) -> Controller:
        return self.controller
