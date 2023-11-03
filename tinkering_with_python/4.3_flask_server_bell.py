

import subprocess
from flask import Flask, render_template, request, jsonify
from pygame import mixer
import time

app = Flask(__name__)

mixer.init()

def play_bell():
    s = mixer.Sound('./bell.mp3')
    s.play()
    time.sleep(2)

@app.route('/bell', methods=['GET'])
def bell():
    play_bell()
    return ("playing bell!")

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)


