from urllib.parse \
    import \
    urlparse, \
    ParseResult

from time import time
import json


class CacheEntry:
    def __init__(
            self,
            href: str
    ):
        self.identifier = None

        self.link_url = None
        self.tokens = None

        self.set_link_url(href)

        self.last_visit = 0

    def is_identifier_none(self) -> bool:
        return self.identifier is None

    def get_identifier(self) -> int:
        return self.identifier

    def set_identifier(
            self,
            value: int
    ):
        self.identifier = value

    def get_link_url(self) -> str:
        return self.link_url

    def set_link_url(
            self,
            value: str
    ):
        self.link_url = value

    def get_tokens(self) -> ParseResult:
        if self.tokens is None:
            self.set_tokens(
                urlparse(
                    self.get_link_url()
                )
            )

        return self.tokens

    def set_tokens(
            self,
            value: ParseResult
    ):
        self.tokens = value

    def set_last_visit(
            self,
            value: int
    ):
        self.last_visit = value

    def get_last_visit(self) -> int:
        return self.last_visit

    def visited(self):
        self.set_last_visit(
            int(
                time()
            )
        )

    def export_to_object(self) -> str:
        return str(
            json.dumps(
                self.to_object()
            )
        )

    def to_object(self):
        return \
            {
                'identifier': self.get_identifier(),
                'link_to': self.get_link_url(),
                'tokens': self.get_tokens(),
                'last_visit': self.get_last_visit()
        }

    def import_values(
            self,
            json_object
    ):
        json_import = json_object

        self.set_identifier(
            int(
                json_import['identifier']
            )
        )
        self.set_tokens(json_import['tokens'])
        self.set_last_visit(
            int(
                json_import['last_visit']
            )
        )
