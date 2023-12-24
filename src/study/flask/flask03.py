from flask import Flask
# 这两个函数用来实现链接的重定向
from flask import redirect, url_for
# 我本来想直接调用别的文件的函数，但是似乎不行，估计是两个文件的app实例不一样
# from flask01 import home

app = Flask(__name__)

@app.route("/<name>")
def user(name):
    return f"Hello {name} !"

@app.route("/admin")
def admin():
    # url_for函数可以直接以字符串作为参数，其可以根据字符串去寻找到其需要的函数
    # url_for函数在调用别的函数的时候添加参数的方式如下所示
    return redirect(url_for("user", name = "Admin"))

if __name__ == "__main__":
    app.run()
    