from flask import Flask
from routes.executeCode import executeCode

app = Flask(__name__)

app.register_blueprint(executeCode, url_prefix='/executeCode')

@app.route('/')
def hello_world():
    return "Hello World5"

if __name__ == "__main__":
    app.run(debug=True, port=3300)