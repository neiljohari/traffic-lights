from flask import Flask
from flask import request
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
chan_list = [16,18,22]
GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, 0)

@app.route("/ha-api")
def api():
    cmd = int(request.args.get('cmd', ''))
    scope = request.args.get('scope', '')

    # TODO: Hash with colors and pins to clean this all up
    if scope == "all":
        GPIO.output(chan_list, cmd)
    elif scope == "red":
        GPIO.setup(chan_list[0], GPIO.OUT)
        GPIO.output(chan_list[0], cmd)
    elif scope == "yellow":
        GPIO.setup(chan_list[1], GPIO.OUT)
        GPIO.output(chan_list[1], cmd)
    elif scope == "green":
        GPIO.setup(chan_list[2], GPIO.OUT)
        GPIO.output(chan_list[2], cmd)
    else:
        print("Don't know what happened")
    return "Great success."
