from flask import Flask, render_template
from routines import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/LEDON")
def ledOn():
    pin17On()
    return("Led on.")

@app.route("/LEDOFF")
def ledOff():
    pin17Off()
    return("Led off.")


### Host on 0.0.0.0 makes site available on local network
### site will be on the host's IP : 5000 (port 5000)
app.run(debug = True, host='0.0.0.0')
