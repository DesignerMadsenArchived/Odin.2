import pprint
from src.crawler.database.CacheDatabase \
    import get_singleton

from src.crawler.database.CacheEntry \
    import CacheEntry


database = get_singleton()
entryList = database.get_list()

