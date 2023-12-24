from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/<name>")
def user(name):
    # 可以用这种方法加载网页模版
    # placeholder-占位符
    # 可以在html中插入python代码，详见index.html文件
    # 同时也可以用python代码插入列表
    return render_template("old_index.html", 
                           pi = 3.14, 
                           placeholder = name,
                           lis = ["van", "en", "ze"])

if __name__ == "__main__":
    app.run()
    