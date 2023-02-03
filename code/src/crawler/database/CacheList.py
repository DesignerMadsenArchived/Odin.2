
from src.crawler.database.CacheEntry \
    import CacheEntry

from src.stats.CounterObject \
    import CounterObject


class CacheList:
    def __init__(self):
        self.list = []
        self.position = None
        self.cached_size = CacheListSize(self)

        self.reset_position()
        self.counter = CounterObject()

    def get_counter(self) -> CounterObject:
        return self.counter

    def set_counter(self, value:CounterObject):
        self.counter = value

    def get_list(self) -> list:
        return self.list

    def set_list(
            self,
            value: list
    ):
        self.list = value

    def has_url_in_set(self, link: str)->bool:

        for idx in range(0, self.size_of()):
            current = self.get_index(idx)

            if current.get_link_url() == link:
                return True

        return False

    def append(
            self,
            value: CacheEntry
    ):
        self.get_list().append(
            value
        )

        self.cached_size.flag_has_changed()

    def remove_at_position(
            self,
            index_position: int
    ):
        self.list.pop(index_position)
        self.cached_size.flag_has_changed()

    def get_index(
            self,
            index_position: int
    ) -> CacheEntry:
        return self.list[index_position]

    def set_position(
            self,
            value: int
    ):
        self.position = value

    def get_position(self) -> int:
        return self.position

    def reset_position(self) -> None:
        self.position = 0

    def size_of(self) -> int:
        return self.cached_size.get_current_size()


class CacheListSize:
    def __init__(
            self,
            list: CacheList
    ):
        self.size = 0

        self.has_changed = False
        self.cache_list = list

    def flag_has_changed(self):
        self.set_is_changed(True)

    def has_state_changed(self) -> bool:
        return self.has_changed

    def set_is_changed(
            self,
            value: bool
    ):
        self.has_changed = value

    def get_size(self) -> int:
        return self.size

    def set_size(
            self,
            size_of: int
    ):
        self.size = size_of

    def get_list_size(self):
        return len(
            self.cache_list.get_list()
        )

    def get_current_size(self):
        if self.has_state_changed():
            self.set_size(
                self.get_list_size()
            )

        return self.get_size()
