from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import inspect

from db_models import db, Todo

app = Flask(__name__)

app.config.from_object('db_config.Config')
db.init_app(app)


# Needs to be a function so it can be called directly from the app or in a gunicorn config file
def initialize_database():
    """Check and initialize the database only if not already created."""
    with app.app_context():
        if not inspect(db.engine).has_table("todo"):
            print("Creating Database")
            db.create_all()
            print("Database Created")
        else:
            print("Database already initialized")

# Initialize the database
initialize_database()

@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

# Allows starting the server by running this script with python instead of flask or gunicorn commands
# see README.md for more on server/prod vs local/dev
if __name__ == "__main__":
    print("Running dev server")
    initialize_database()
    app.run(debug=True)

