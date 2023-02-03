from redis \
    import Redis

# Caches the crawlers current state
class HistoryDatabase:
    def __init__(
            self,
            hostname: str = '127.0.0.1',
            port: int = 6379,
            database: int = 2
    ) -> None:
        self.database = Redis(
            host=hostname,
            port=port,
            db=database
        )

    def __del__(self) -> None:
        self.get_database().close()

    def get_database(self) -> Redis:
        return self.database

    def set_database(
            self,
            value: Redis
    ) -> None:
        self.database = value


