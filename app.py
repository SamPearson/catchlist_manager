from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

#Allows starting the server by running this file from python instead of running flask
if __name__ == "__main__":
    app.run(debug=True)


# 7 minutes in