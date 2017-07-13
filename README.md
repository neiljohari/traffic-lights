# Traffic Lights
🚦 Raspberry Pi project to revive an old traffic light

## Background
I've had a traffic light in my backyard for a while. As a fun side project, I wanted to make it work again. The code in this repo runs on the Raspberry Pi Zero W used in the project.

## Setup
My pi is connected to a relay module board. The `web_app.py` file is a Flask web server that I have as a startup script. This web app allows me to switch on/off certain lights or all of them using a web endpoint. The `fauxmo.py` is a Python3 updated version of makermusings/fauxmo that also runs as a startup script.

With this setup, I can use Echo or Echo Dot to control the traffic light. Since its being controlled through a web endpoint, I plan to also get CS:GO gamestate integrations going, and a color organ with Spotify. 

