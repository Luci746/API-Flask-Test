from flask import Flask
from flask import Blueprint
def createApp():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '<p>Olá flask</p>'
    

    return app