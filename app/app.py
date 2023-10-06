import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
from routes.user_routes import user_bp
from routes.stock_routes import stock_bp
# Load environment variables from .env file
load_dotenv()

# Determine the environment (default to 'development' if not set)
environment = os.getenv('ENV', 'development')

# Import the appropriate configuration file based on the environment
if environment == 'production':
    from config.production import DATABASE_URI
elif environment == 'development':
    from config.development import DATABASE_URI
else:
    raise ValueError("Invalid environment specified in ENV variable.")


# Create a Flask application
app = Flask(__name__)


app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(stock_bp, url_prefix='/stock')

# Create a database engine
engine = create_engine(DATABASE_URI)

# Create a session class
Session = sessionmaker(bind=engine)

# Create tables in the database
Base.metadata.create_all(engine)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Welcome to your Flask app!'

# Run the Flask app if this file is executed
if __name__ == '__main__':
    app.run(debug=True)