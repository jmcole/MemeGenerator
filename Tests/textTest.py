"""Tests Quote Generator."""


from QuoteEngine import Ingestor


def setup():
    """Load all resources."""
    quote_files = ['../_data/DogQuotes/DogQuotesTXT.txt',
                   '../_data/DogQuotes/DogQuotesDOCX.docx',
                   '../_data/DogQuotes/DogQuotesPDF.pdf',
                   '../_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        for quote in Ingestor.parse(file):
            quotes.append(quote)
            print(quote)
    return quotes


quotes = setup()
