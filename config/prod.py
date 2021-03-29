import secrets
import os

DEBUG =False
SECRET_KEY=secrets.token_hex(32)
SQLALCHEMY_DATABASE_URI= os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS=False