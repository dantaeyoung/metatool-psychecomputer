

import subprocess
from flask import Flask, render_template, request, jsonify
from pygame import mixer
import webbrowser
import time

app = Flask(__name__)

mixer.init()


def open_arena():
    webbrowser.open('https://www.are.na/', new=2)


def write_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)


mixer.init()

def play_bell():
    s = mixer.Sound('./bell.mp3')
    s.play()
    time.sleep(2)




@app.route('/bell', methods=['GET'])
def bell():
    play_bell()
    return ("playing bell!")       


@app.route('/grasshopper', methods=['GET'])
def grasshopper():
    write_to_file('data.txt', '! SelAll Delete Enter !')
    return ("sending data to grasshopper!")

@app.route('/openarena', methods=['GET'])
def openarena():
    open_arena()
    return ("opening arena!")


@app.route('/bell-and-arena', methods=['GET'])
def bellarena():
    play_bell()
    open_arena()
    return ("playing bell and opening arena!")       


@app.route('/resetrhino', methods=['GET'])
def resetrhino():
    write_to_file('data.txt', '! SelAll Delete Enter !')
    return ("resetting rhino!")


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)


