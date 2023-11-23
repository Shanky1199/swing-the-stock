import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base
from dotenv import load_dotenv
from flask_migrate import Migrate
from routes.user_routes import user_bp
# from routes.stock_routes import stock_bp

# Load environment variables from .env file
load_dotenv()

def create_app(test_config=None):
    # Create a Flask application
    app = Flask(__name__)

    # Load configuration from the respective environment
    if test_config is None:
        if os.getenv('FLASK_ENV') == 'production':
            app.config.from_object('config.ProductionConfig')
        else:
            app.config.from_object('config.DevelopmentConfig')
    else:
        app.config.from_mapping(test_config)

    # Initialize database
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db_session = scoped_session(sessionmaker(bind=engine))
    Base.query = db_session.query_property()

    # Initialize Flask-Migrate
    Migrate(app, engine)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/user')
    # app.register_blueprint(stock_bp, url_prefix='/stock')

    # Create tables in the database
    with app.app_context():
        Base.metadata.create_all(engine)

    # Root route
    @app.route('/')
    def index():
        return "Hello"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])