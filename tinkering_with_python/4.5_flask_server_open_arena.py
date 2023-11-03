

import subprocess
from flask import Flask, render_template, request, jsonify
from pygame import mixer
import webbrowser
import time

app = Flask(__name__)

mixer.init()


def open_arena():
    webbrowser.open('https://www.are.na/', new=2)

@app.route('/open', methods=['GET'])
def open_arena():
    open_arena()
    return ("opening arena!")



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)


