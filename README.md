# Overview

[![Udacity](https://upload.wikimedia.org/wikipedia/commons/e/e8/Udacity_logo.svg)](https://udacity.com)

This project is part of the Udacity [Intermediate Python Course](https://www.udacity.com/course/intermediate-python-nanodegree--nd303). The goal of this project was to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. The MemeGenerator application accepts various file types, including .txt, .docx, .pdf, and .csv. User input is accepted via CLI, as well as through a web interface.

This project makes use of [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [Pillow](https://pillow.readthedocs.io/en/stable/) libraries. It is built upon [Python 3.9](https://www.python.org/downloads/)


## Install Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To Clone, you'll need to install [GIT CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

```sh
$ git clone https://github.com/jmcole/MemeGenerator.git 

$ cd /src

$ pip install -r requirements.txt

```

# Live 
Click here ---> [MemGenerator](https://memegenerator-app.herokuapp.com/) to utilize the live version hosted on [Heroku](https://devcenter.heroku.com/).

# Operation

The MemeGenerator can accept user input through either the CLI tool or the web interface.

## CLI Interface
From the project root-Using Git Bash or other Command Line Interface:

All Memes will be created in the /tmp directory.

No arguments will generate a random Meme
```sh
$ python3 meme.py
./tmp/img.jpg
```
You can specify Author
```sh
$ python3 meme.py --author Stinky
./tmp/img.jpg
```
You can specify Body
```sh
$ python3 meme.py --body Bark
./tmp/img.jpg
```
You can specify Path to image
```sh
$ python3 meme.py --path ./_data/photos/dog/xander_2.jpg
./tmp/img.jpg
```
You can also use Body and Author

```sh
$ python3 meme.py --body Bark --author Hero
./tmp/img.jpg
```
Help is accesible with the --h command.
```sh
$ python3 meme.py --help
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Creates Meme

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      Image file path
  --body BODY      Quote Body
  --author AUTHOR  Author
```
## Web Interface

Running app.py will start the Flask Application.

```sh
$ python3 app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Navigate to http://127.0.0.1:5000.

## Random Meme Generator
The WebApp allows the random creation of Memes. Just Click the **Random button** to see a new meme.
## Custom Meme Generator
Click the **Creator Button** to create a custom Meme. Enter a link to an image, such as https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/769px-Cat03.jpg. Enter Quote Body and Author and click **Create Meme!**.

# Module Structure

###  `app.py`- Responsible for Web Application
###  `meme.py`- Responsible for CLI application

## MemeEngine
The MemeEngine utilizes the Pillow Library to draw the quote text and author on the image.
## QuoteEngine
The QuoteEngine parses the quote files through specific Ingestors and provides a stream of quotes through the main Ingestor file in order to generate the Meme text.
## Requirements

Specific requirements are included in the Git package. MemeEngine relies heavily on Flask and  Pillow libraries. 

## Tests

The Tests folder contains some simple test files that were useful in troubleshooting Memebuilder during its development.









![Python](https://www.python.org/static/community_logos/python-powered-w-100x40.png)


