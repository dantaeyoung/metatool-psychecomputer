

import subprocess
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    result = 2 + 2
    return str(result)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)


