from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "van"
app.permanent_session_lifetime = timedelta(hours=2, minutes=30)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # 这使得session会调用上面的permanent_session_lifetime的值
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
             
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)