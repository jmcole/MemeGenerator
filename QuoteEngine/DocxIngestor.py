"""Reads Word file and creates List."""


from typing import List
from docx import Document
from .ingestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class Method to parse WORD file."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Word file and Creates List."""
        doc = Document(path)
        quotes = []
        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.replace('"', '').split('-')
                quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(quote)
        return quotes
