from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    # 这一节主要讲了模版文件的使用以及bootstrap网站的利用
    # 这样子我们可以写一个模版网页出来，后续根据自己的需要对模版填充内容，也可以借鉴bootstrap已有的模版
    # 注意这里base文件需要在template目录或者其子目录下
    # 我尝试将其放在flask目录里，但是../base.html语法好像没生效
    return render_template("index.html", content="flask05.py")

if __name__ == "__main__":
    # 这可以即时更新网站，而不需要我们每次重复执行
    app.run(debug=True)
    