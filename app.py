from flask import Flask, request,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from .models import UserModel

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///test.db"
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy()
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    return "Welcome to Flask User page."

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return render_template("users/users.html")
    elif request.method == "POST":
        return render_template("users/users.html")
    return "Hello"



if __name__ == "__main__":
    app.run(debug=True)