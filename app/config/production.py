# development.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read database URL from environment variables
DATABASE_URI = os.getenv('PROD_DATABASE_URI')
