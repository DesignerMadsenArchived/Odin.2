class HistoryEntry:
    def __init__(self):
        self.entryKey = str()
        self.href = str()
        self.last_visit = None

    def get_entry_key(self) -> str:
        return self.entryKey

    def set_entry_key(
            self,
            value: str
    ):
        self.entryKey = value

    def get_href(self) -> str:
        return self.href

    def set_href(
            self,
            href: str
    ):
        self.href = href
