from flask import Flask
from servidor import database
from asyncio import run

def create_app():
    app = Flask(__name__)
    run(database.app_init())
    with app.app_context():
        from servidor import routes
    return app

    