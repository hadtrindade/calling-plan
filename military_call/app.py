from flask import Flask
from military_call.ext import site

def create_app():
    """
    Factory principaç

    Returns:
        [obg]: [app flask]
    """
    app = Flask(__name__)
    site.init_app(app)
    return app
