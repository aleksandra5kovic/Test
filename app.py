"""Flask app."""

from flask import Flask
from models import Comment

app = Flask(__name__)


@app.route("/")
def index():
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title></title>
    </head>

    <body>
        <heading>Welcome!</heading>
    </body>

    </html>
    """


@app.route("/comments")
def comments():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title></title>
    </head>

    <body>
        {}
    </body>

    </html>
    """
    table = Comment.table()
    return page.format(table)