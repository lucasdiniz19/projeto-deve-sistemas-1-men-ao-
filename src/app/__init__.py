import os
from flask import Flask
from dotenv import load_dotenv
from .extensions import db
from flask_migrate import Migrate
from .models import User, Categoria, Lancamento, Historico

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    return app