# Flask Application
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Welcome to the Flask Application!</h1>'

if __name__ == '__main__':
    try:
        import flask
    except ImportError:
        import os
        os.system('pip install flask')
        import flask

    app.run(host='0.0.0.0', port=80)
