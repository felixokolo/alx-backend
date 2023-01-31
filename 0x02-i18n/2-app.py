#!/usr/bin/env python3
"""Flask-Babel app
"""

from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class
    """
    LANGUAGES = ["en", "fr"]

    @babel.localeselector()
    def get_locale(self) -> str:
        """Get locale config
        """
        return request.accept_languages.best_match(Config.LANGUAGES)

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
    return render_template('0-index.html')

if __name__ == '__main__':
    config = Config()
    babel.get_locale = config.get_locale()
    babel.get_timezone = config.get_timezone()
    app.run('0.0.0.0')