from flask import Flask, render_template, jsonify
import os
from funcs.db import Db

app = Flask(__name__, template_folder='templates')
db = Db()


@app.route("/")
def home():
    todos = db.find_all('todos')
    return render_template('home.html', todos=list(todos))

@app.route("/todo/<importance_val>")
def get_todo(importance_val):
    todos = db.find('todos', {"importance": int(importance_val)})
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5110)