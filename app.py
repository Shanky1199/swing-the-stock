import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask
app = Flask(__name__, instance_relative_config=True)

# Load environment-specific configuration
config_name = os.getenv('ENV', 'development').capitalize()
app.config.from_object(f'app.config.development.{config_name}Config')

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the app and db
migrate = Migrate(app, db)

# Import and register blueprints if you have any
# from app.controllers.some_controller import some_blueprint
# app.register_blueprint(some_blueprint)

if __name__ == '__main__':
    app.run()
