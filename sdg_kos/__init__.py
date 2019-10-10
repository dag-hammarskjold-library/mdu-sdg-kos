from flask import Flask, request
from app.cache import cache
from flask_babel import Babel, gettext
from app.config import Config

# Initialize your application.
app = Flask(__name__)
babel = Babel(app)
#cache.init_app(app)

@babel.localeselector
def get_locale():
    locale = request.args.get('lang',request.accept_languages.best_match(Config.available_languages.keys()))
    #print(locale)
    return locale

from app.routes import *