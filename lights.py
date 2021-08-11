from flask import Flask, render_template, request
from routines import *
import sys
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
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

@app.route("/4On")
def fourOn():
    pin17_18_20_21On()
    return("Pins 17, 18 20, 21 On")

@app.route("/4Off")
def fourOff():
    pin17_18_20_21Off()
    return("Pins 17, 18 20, 21 Off")

### cleanExit not working as intended, file does not stop running

@app.route("/StopRunning")
def finish():
    print("Server is shutting down.")
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if shutdown is None:
        raise RuntimeError('Function is unavailable.')
    else:
        shutdown()
        return "Shutting down!"
    cleanExit()



### Host on 0.0.0.0 makes site available on local network
### site will be on the host's IP : 80 (port 80)/ might not need to specify port 80 as
### this is the default HTTP port
try:
    app.run(debug = True, host='0.0.0.0', port = 80)
except SystemExit:
    pass
except Exception as e:
    print(e)

finally:
    cleanExit()
    sys.exit(0)
