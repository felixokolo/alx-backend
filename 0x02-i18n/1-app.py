#!/usr/bin/env python3
"""Flask-Babel app
"""

from flask_babel import Babel
from flask import Flask

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class
    """
    LANGUAGES = ["en", "fr"]

    def get_locale():
        """Get locale config
        """
        return "en"

    def get_timezone():
        """
        Get timezone config
        """
        return "UTC"


if __name__ == '__main__':
    babel.get_locale = Config.get_locale()
    babel.get_timezone = Config.get_timezone()
    app.run('0.0.0.0')
