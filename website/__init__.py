#this __init__.py will make the website folder a package.
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asd1234gy12bhfhbahbfgahbfhqweilovemiloliit'

    #we have blue prints now, so we initialize them
    
    from .view import view
    from .auth import auth

    #register blueprint
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app



