"""app/catalog/__init__.py"""
from flask import Blueprint
main = Blueprint('main', __name__, template_folder='templates')


from app.catalog import routes # import route at bottom to avoid cross import issues