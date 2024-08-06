from flask import Flask
from routes.submission import submission

app = Flask(__name__)

app.register_blueprint(submission, url_prefix='/submission')

@app.route('/actuator/health')
def hello_world():
    return "{STATUS: 'UP'}"

if __name__ == "__main__":
    app.run(debug=True, port=4401)