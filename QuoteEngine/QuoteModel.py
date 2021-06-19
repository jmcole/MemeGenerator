"""Creates QuoteModel Class."""


class QuoteModel():
    """A class that represents a quote and aauthor."""

    def __init__(self, body, author):
        """Construct QuoteModel Class."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent QuoteModel as String."""
        return f'{self.body} - {self.author}'
