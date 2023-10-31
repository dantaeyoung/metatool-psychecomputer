import subprocess
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/execute-applescript', methods=['POST', 'GET'])
def execute_applescript():
    name = request.args.get('name', 'dan')
    print(name)
    # Execute the AppleScript using osascript
    script = '''
    do shell script "afplay /System/Library/Sounds/Ping.aiff"
    display dialog "Hello, ''' + name + ''' " buttons {"OK"} default button "OK" giving up after 5
    '''
    subprocess.run(['osascript', '-e', script])

    # Respond with an acknowledgment
    response_data = {
        "status": "success",
        "message": "Webhook data received and processed successfully."
    }

    return jsonify(response_data), 200  # 200 indicates a successful response

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


