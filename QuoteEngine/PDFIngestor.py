"""Creates List from PDF File."""


from typing import List
import subprocess
import os
import random
from .ingestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class Method that Parses PDF File for QuoteModel."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF and Creates List."""
        tmp = f'.{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', '-raw', path, tmp])
        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.replace('"', '').strip('\n\r').strip()
            if len(line):
                parse = line.split(' - ')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)
        file_ref.close()
        os.remove(tmp)
        return quotes
