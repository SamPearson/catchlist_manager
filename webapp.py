from flask import Flask, render_template, request, redirect, url_for
from db_config import initialize_database
from db_models import db, Todo

app = Flask(__name__)

app.config.from_object('db_config.Config')
db.init_app(app)


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


@app.route("/delete/<int:todo_id>", methods=["DELETE"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return "Todo not found", 404
    db.session.delete(todo)
    db.session.commit()
    return "", 204  # No Content response (DELETE success), reloading happens in javascript


# Allows starting the server by running this script with the python3 command instead of flask or gunicorn commands
# only do this on local/dev. see README.md for more on server/prod vs local/dev
if __name__ == "__main__":
    initialize_database(app)  # handled in a config file when running on a server
    app.run(debug=True, port=5000)

