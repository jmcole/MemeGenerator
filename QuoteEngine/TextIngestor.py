"""Parse TXT File and QuoteModel List."""
from os import path
from .QuoteModel import QuoteModel
from .ingestorInterface import IngestorInterface
from typing import List


class TextIngestor(IngestorInterface):
    """Class TxtIngestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TXT file and create QuoteModel list."""
        quotes = []
        with open(path, encoding='utf-8-sig') as doc:
            lines = doc.readlines()
            for line in lines:
                quote = line.strip().split(' - ')
                quotes.append(QuoteModel(quote[0], quote[1]))
        return quotes
