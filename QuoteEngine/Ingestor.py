"""Main Ingestor Class."""


from QuoteEngine.DocxIngestor import DocxIngestor
from typing import List
from .ingestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Class Method to check allowed extensions."""

    ingestors = [TextIngestor, PDFIngestor, CSVIngestor, DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Define allowed extensions."""
        for ingestor in cls.ingestors:
            TextIngestor.allowed_extensions = '.txt'
            CSVIngestor.allowed_extensions = '.csv'
            PDFIngestor.allowed_extensions = '.pdf'
            DocxIngestor.allowed_extensions = '.docx'
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
