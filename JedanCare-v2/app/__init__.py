from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

# Import your models here
from app.models import  *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///JedanCare.db'

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)

    # Create the database tables within the app context
    with app.app_context():
        db.create_all()

    from app.routes import auth_bp
    app.register_blueprint(auth_bp)
    
    from app.routes import main_bp
    app.register_blueprint(main_bp)


    return app

