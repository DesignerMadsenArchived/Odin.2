import redis

from base.counter \
    import Counter


class History:
    def __init__(self):
        self.rotation = Counter()

        self.list = []

        self.tree = {}

    def insert_last_url(
            self,
            url: str
    ):
        self.list.append(url)

        self.routine()

    def routine(self):
        self.rotation.increment()

        if self.rotation.get_value() % 500 == 0:
            self.routine_status()
            self.list.sort()

    def is_in_history(self, url: str):
        for idx in range(0, len(self.list)):
            current = self.list[idx]

            if url == current:
                print("hit")
                return True

        return False

    def size(self):
        return len(self.list)

    def routine_status(self):
        print(self.list)
