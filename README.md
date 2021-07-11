# RoomLights
Web app and python code that will (eventually) control a strip of RGB LEDs connected to a Rasperry Pi's GPIO pins.

### Structure

As the project is set up using the Python web framework, Flask, the structure of the files is important. 
Flask looks for html files in the templates folder with the `render_template` function. Although, since the web app makes use of tabs, only one html template is currently used. 

Within the static folder are the folders `js` and `css` which obviously contain the javascript and css to make the web app function and look pretty 🎉 

For the sake of tidiness, I have separated the python functions which control the lights into a separate file which is imported in `lights.py`.

### Operation

The `lights.py` file can be run on anything for testing purposes this will start a server which can be accessed at the host's ip, port 5000. e.g. `192.168.0.1:5000`.
The proper use however is to run the file on a Rasperry Pi, or possibly another device with GPIO pins.


