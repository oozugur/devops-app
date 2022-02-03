from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my app!"

@app.route('/hi/<username>')
def greet(username):
    return f"Hi {username}, Welcome to my app!"