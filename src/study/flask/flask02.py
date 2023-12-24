from flask import Flask

app = Flask(__name__)

# 使用这种语法，使得我们可以很方便的获取到网址中的参数

@app.route("/<name>")
def user(name):
    # 字符串前面加上f代表这是一个格式化(format)字符串(自python3.6之后引入)
    # 它允许在字符串中嵌入表达式，并在运行时进行求值
    return f"Hello {name} !"

if __name__ == "__main__":
    app.run()