from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)

# methods参数指定了调用login函数所允许的方法
@app.route("/login", methods=["GET", "POST"])
def login():
    # 这个判断语句用来判断发送http请求时，使用的是什么方式
    if request.method == "POST":
        # request中包括http请求的各种属性，这里用form来获取表单数据
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
        return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)