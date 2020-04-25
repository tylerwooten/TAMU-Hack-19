import RPi.GPIO as GPIO

from flask import Flask
from flask import request
 
app = Flask(__name__)


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

@app.route('/<action>')
def ledAction(action):
    if action == 'on':
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
    if action == 'off':
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
    return ''
 
@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    job = data['job']
    state = data['state']
    print("recieved post request: " + action)
    if job == 'drive':
        if state == 'on':
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.HIGH)
        if state == 'off':
            GPIO.output(7, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
    if job == 'dispense':
        if state == 'on':
            GPIO.output(13, GPIO.HIGH)
        if state == 'off':
            GPIO.output(13, GPIO.LOW)
        
 
app.run(debug=True, host='0.0.0.0')
#app.run(host='127.0.0.1', port= 8090)

