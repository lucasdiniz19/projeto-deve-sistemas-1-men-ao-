import os
from flask import Flask
from dotenv import load_dotenv
from .extensions import db, migrate 

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')

    db.init_app(app)
    migrate.init_app(app, db)

  
    from .routes import bp
    app.register_blueprint(bp)
    
    return app