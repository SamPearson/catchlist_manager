from flask import Flask, request, jsonify
from db_models import db, Todo
from db_config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Use the shared config
db.init_app(app)

# Example endpoint: fetch all
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.as_dict() for todo in todos])  # Convert each To-do to dict for JSON response

# Example endpoint: fetch one by ID
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    if todo:
        return jsonify(todo.as_dict())
    else:
        return jsonify({"message": "Todo not found"}), 404

# Example endpoint: create
@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()  # Expect JSON input
    new_todo = Todo(title=data.get('title'), complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.as_dict()), 201

# Example endpoint: update one by ID
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo = db.session.get(Todo, todo_id)
    if todo:
        todo.title = data.get('title', todo.title)
        todo.complete = data.get('complete', todo.complete)
        db.session.commit()
        return jsonify(todo.as_dict())
    else:
        return jsonify({"message": "Todo not found"}), 404

# Example endpoint: delete one by ID
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted"})
    else:
        return jsonify({"message": "Todo not found"}), 404


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
