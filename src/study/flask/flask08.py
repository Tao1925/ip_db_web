from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session
from flask import flash
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
        flash("login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("already login")
            return redirect(url_for("user"))
        else:
            return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template(url_for("user.html", user=user))
    else:
        flash("you are not log in!")
        return redirect(url_for("login"))
             
@app.route("/logout")
def logout():
    flash(f"you have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)