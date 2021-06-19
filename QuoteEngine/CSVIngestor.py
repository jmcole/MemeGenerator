"""Reads CSV file."""


from typing import List
import pandas as pd
from .ingestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class Method to read CSV file."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read CSV File and create List of Objects."""
        df = pd.read_csv(path, header=0)
        quotes = []
        for index, row in df.iterrows():
            quote = QuoteModel(row["body"], row["author"])
            quotes.append(quote)
        return quotes
