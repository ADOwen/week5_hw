from flask import Flask

from .shop.routes import shop

from .auth.routes import auth

app = Flask(__name__)

app.register_blueprint(shop)

app.register_blueprint(auth)

from app import routes