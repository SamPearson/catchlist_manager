from api import app
from db_config import initialize_database


def on_starting(server):
    initialize_database(app)
