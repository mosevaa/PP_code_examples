from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello_world():
    return {'data': 'HelloWorld'}


@app.route('/data', methods=['GET'])
def data():
    return {'name': 'John', 'surname': 'Jackson', 'age': 21}
