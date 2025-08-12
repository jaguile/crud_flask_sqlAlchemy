from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    SECRET_KEY = environ.get('SECRET_KEY')
    SQLITE_FILE_PATH = environ.get('SQLITE_FILE_PATH')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir + SQLITE_FILE_PATH
    SQLALCHEMY_ECHO=environ.get('SQLALCHEMY_ECHO')