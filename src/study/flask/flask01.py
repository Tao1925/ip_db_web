
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# 1. basic
# 
# browser -> http://127.0.0.1:5000
@app.route('/')
def index():
    return 'Index Page'

# 2. 
@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/<name>')
def call(name):
    return f"Hello, {escape(name)}!"