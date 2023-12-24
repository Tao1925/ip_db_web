from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
        return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)