#!/usr/bin/env python3
"""
Flask app with dynamic locale detection based on request headers.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Cofiguration class for the app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Return user dict if ID was found and login_as was passed, else None."""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Sets the current user on `flask.g` before each request."""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    # From URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # From user
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    # From request header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    # Default
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """Render the home page."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
