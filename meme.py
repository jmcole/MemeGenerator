"""Generates Meme from Image Path and Quote."""


import os
import random
import argparse
import shutil

# Import Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def random_gen(quote):
    """Generate Random Quote."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
    quote = random.choice(quotes)
    return quote


def generate_meme(path=None, body=None, author=None):
    """Generate Meme from Image Path and Quote."""
    img = None
    quote = None
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote = random_gen(quote)
        body = quote.body
    if author is None:
        quote = random_gen(quote)
        author = quote.author
    quote = QuoteModel(body, author)
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creates Meme")
    # path - path to an image file
    parser.add_argument('--path', type=str,
                        default=None, help="Image file path")
    # body - quote body to add to the image
    parser.add_argument('--body', type=str,
                        default=None, help="Quote Body")
    # author - quote author to add to the image
    parser.add_argument('--author', type=str,
                        default=None, help="Author")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
