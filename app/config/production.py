from .default import Config

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'your_production_database_uri'
    # Other production-specific settings...
