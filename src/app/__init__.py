import os
from flask import Flask
from dotenv import load_dotenv
from database import db # ou de onde vier seu db
from flask_migrate import Migrate
from .extensions import db, migrates

load_dotenv() # Isso carrega o arquivo .env

def create_app():
    app = Flask(__name__)
    
    # Pega a URL do banco do arquivo .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db) # Isso ativa o comando 'flask db'

    # Registre suas rotas aqui embaixo...
    return app