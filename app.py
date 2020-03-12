from flask import Flask, render_template
import os
from db import Db

app = Flask(__name__, template_folder='templates')
# db = Db()


@app.route("/")
def home():
    # todos = db.find_all('todos')
    # return render_template('home.html', todos=list(todos))
    return "Hello"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)