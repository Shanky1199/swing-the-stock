import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)

    # Load environment-specific configuration
    app.config.from_object(config_filename)

    # Initialize db with app
    db.init_app(app)

    # Flask-Migrate initialization
    migrate = Migrate(app, db)

    # Import and register blueprints...
    # from yourapplication.some_module import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app

# Create an instance of the app
config_name = os.getenv('FLASK_CONFIGURATION', 'development')
app = create_app(f'config.{config_name.capitalize()}Config')

if __name__ == '__main__':
    app.run()
