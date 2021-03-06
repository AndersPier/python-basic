from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! New - 27-04-2022"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
