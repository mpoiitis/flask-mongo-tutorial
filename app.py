from flask import Flask, render_template

from db import Db

app = Flask(__name__, template_folder='templates')
db = Db()


@app.route("/")
def home():
    todos = db.find_all('todos')
    return render_template('home.html', todos=list(todos))


if __name__ == "__main__":
    app.run(debug=True, host='https://mpoiitis.netlify.com', port=5000)