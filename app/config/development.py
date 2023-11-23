from .default import Config

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'your_development_database_uri'
    # Other development-specific settings...
