import os
from datetime import timedelta

class Config:
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, '../run.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  