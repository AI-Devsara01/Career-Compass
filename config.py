import os

class Config:
    # Secret Key for sessions
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug mode
    DEBUG = True
