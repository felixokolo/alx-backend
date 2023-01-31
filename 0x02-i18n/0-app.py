#!/usr/bin/env python3
"""Flask-Babel app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    """
    Root route
    renders a welcome html page
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
