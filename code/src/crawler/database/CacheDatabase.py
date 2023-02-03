from src.crawler.database.CacheEntry \
    import CacheEntry

from src.crawler.database.CacheList \
    import CacheList

from redis \
    import Redis

import json


# Caches the crawlers current state
class CacheDatabase:
    def __init__(
            self,
            hostname: str = '127.0.0.1',
            port: int = 6379,
            database: int = 1
    ) -> None:
        self.database = Redis(
            host=hostname,
            port=port,
            db=database
        )

        self.list = CacheList()

    def __del__(self) -> None:
        self.get_database().close()

    def get_database(self) -> Redis:
        return self.database

    def set_database(
            self,
            value: Redis
    ) -> None:
        self.database = value

    def load_state(self):
        client = self.get_database()
        highest_id = 0

        result = client.keys('CachedElement:*')

        for e in result:
            formatted = e.decode()

            key, id = str(formatted).split(':')
            id_conv = int(id)

            if highest_id <= id_conv:
                highest_id = id_conv

            value_returned = client.get(formatted)
            obj = json.loads(value_returned.decode())

            entry_found = CacheEntry(
                obj['link_to']
            )

            entry_found.import_values(obj)

            self.get_list().append(entry_found)

        self.get_list().get_counter().set_position(highest_id)

    def save_state(self):
        client = self.get_database()

        for idx in range(0, self.list.size_of()):
            print(idx)

            element = self.get_list().get_index(idx)

            if element.is_identifier_none():
                element.set_identifier(
                    self.generate_id()
                )

            key_path = self.__get_key(
                element.get_identifier()
            )

            client.set(
                key_path,
                str(
                    element.export_to_object()
                )
            )

        client.save()

    def __get_key(self, id: int) -> str:
        return 'CachedElement:' + str(id)

    def generate_id(self):
        counter = self.get_list().get_counter()
        counter.increment()

        id = counter.get_position()

        return id

    def get_list(self) -> CacheList:
        return self.list

    def set_list(
            self,
            value: CacheList
    ) -> None:
        self.list = value


singleton = None


def set_singleton(
        value: CacheDatabase
) -> None:
    global singleton
    singleton = value


def get_singleton() -> CacheDatabase:
    global singleton

    if singleton is None:
        set_singleton(
            CacheDatabase()
        )

    return singleton

