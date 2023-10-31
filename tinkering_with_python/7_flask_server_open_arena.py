

import subprocess
from flask import Flask, render_template, request, jsonify
from pygame import mixer
import time

app = Flask(__name__)

mixer.init()

def open_arena():
    ## code here

@app.route('/open', methods=['GET'])
def open():
    open_arena()
    return ("opening arena!")

@app.route('/bellui', methods=['POST', 'GET'])
def bellui():
    return render_template('bellui.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)


