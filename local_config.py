from sqlalchemy import inspect


def initialize_database(app):
    """Check and initialize the database only if not already created."""
    with app.app_context():
        if not inspect(app.extensions['sqlalchemy'].db.engine).has_table("todo"):
            print("Creating Database")
            app.extensions['sqlalchemy'].db.create_all()
            print("Database Created")
        else:
            print("Database already initialized")
