import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
