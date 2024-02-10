import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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

# Create the SQLAlchemy engine
db_url = os.getenv('DEV_DATABASE_URI')  # Adjust this to your actual database URL
engine = create_engine(db_url)

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# Import and register blueprints
from app.routes.user_routes import user_bp
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()