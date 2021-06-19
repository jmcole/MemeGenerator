"""Create Web Application."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
import shutil

# Import Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in quote_files variable
    quotes = []
    for i in quote_files:
        for quote in Ingestor.parse(i):
            quotes.append(quote)

    images_path = "./_data/photos/dog/"

    # Find images within the images images_path directory
    imgs = os.listdir(images_path)
    imgs = [images_path + item for item in imgs]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Select a random image from imgs array
    img = random.choice(imgs)
    # select a random quote from the quotes array
    quote = random.choice(quotes)
    # Create path
    path = meme.make_meme(img, quote.body, quote.author)
    template = render_template('meme.html', path=path)
    if template is None:
        abort(404, description="Resource not found")
    return template


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    template = render_template('meme_form.html')
    if template is None:
        abort(404, description="Resource not found")
    return template


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if request.method == 'POST':

        # Get info from web form
        img_url = request.form.get('image_url', default=None)
        body = request.form.get('body', default=None)
        author = request.form.get('author', default=None)
        # fetch image from a user submitted URL
        r = requests.get(img_url)
        # save to temp file and make path
        with open("temp.jpg", 'wb') as f:
            f.write(r.content)
        img = "temp.jpg"
        path = meme.make_meme(img, body, author)
        # remove file
        os.remove("temp.jpg")

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
