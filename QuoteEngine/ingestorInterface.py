"""Interfaces Ingestor and Document Ingestors."""

from abc import ABC, abstractmethod
from typing import List
import os
from .QuoteModel import QuoteModel


class IngestorInterface():
    """Class Method that interfaces Ingestor."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """True if file can be Ingested."""
        ext = os.path.splitext(path)[-1].lower()
        return ext in cls.allowed_extensions

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Raise exception if file cannot be parsed."""
        if not cls.can_ingest(path):
            raise Exception('Error File Cannot Be Read')
