from flask import Flask
from flask_bootstrap import Bootstrap #2
from app.config import Config
from .routes.personajesRyM import personajes_ruta


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)                      #2

    app.register_blueprint(personajes_ruta)
    return app


