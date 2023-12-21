from flask import Flask

app = Flask(__name__) # 创建一个flask的实例

# 这样加注解将会在所有访问该网址的时候，无论后面跟着的路径是什么，都返回这个hello字符串
@app.route("/")
def home():
    return "Hello! \n <h1>HELLO</h1>"

if __name__ == "__main__":
    app.run()