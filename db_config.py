from sqlalchemy import inspect
from db_models import db


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def initialize_database(app):
    """Check and initialize the database only if not already created."""
    with app.app_context():
        if not inspect(app.extensions['sqlalchemy'].db.engine).has_table("todo"):
            print("Creating Database")
            app.extensions['sqlalchemy'].db.create_all()
            print("Database Created")
        else:
            print("Database already initialized")
