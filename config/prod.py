import secrets

DEBUG =False
SECRET_KEY=secrets.token_hex(32)
SQLALCHEMY_DATABASE_URI='postgresql://postgres:Ogo1pet2andy3@localhost/catalog_db'
SQLALCHEMY_TRACK_MODIFICATIONS=False