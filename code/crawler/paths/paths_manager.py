from crawler.paths.facade_manager \
    import FacadeManager


class PathManager(FacadeManager):
    def __init__(
            self,
            history,
            buffer
    ):
        super().__init__(
            history,
            buffer
        )

    def run(self):
        for idx in range(
                0,
                self.size()
        ):
            current = self.index(idx)

            f = current.execute()

            for e in f:
                if not (e is None):
                    self.buffer.append(e)
                    print("inserted to buffer: " + str(e))

    def update(self):
        pass








