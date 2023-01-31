#!/usr/bin/env python3
"""Flask-Babel app
"""

from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class
    """
    LANGUAGES = ["en", "fr"]

    def get_locale(self) -> str:
        """Get locale config
        """
        return "en"

    def get_timezone(self) -> str:
        """
        Get timezone config
        """
        return "UTC"


@app.route("/")
def welcome():
    """
    Root route
    renders a welcome html page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    config = Config()
    app.config['BABEL_DEFAULT_LOCALE'] = config.get_locale()
    app.run('0.0.0.0')
