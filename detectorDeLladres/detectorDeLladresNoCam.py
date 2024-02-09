import os
import datetime
import http.client, urllib
from gpiozero import MotionSensor 

pirPin = 16

pir = MotionSensor(pirPin)


def enviaMensaje(mensaje):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "awq42rfkakrn9t9v3rak1jc1wg9po8",  #YOUR TOKEN CODE
    "user": "unzod5y5ynqjrdywft5i1x9bxqtibf",  #YOUR USER CODE
    "message": mensaje,
  }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    
    
while True:
    print("Buscando movimiento...")
    pir.wait_for_motion()
    print("Movimiento detectado!")

    now = datetime.datetime.now()
    timeStamp = str(now.strftime("%Y-%m-%d_%H:%M:%S"))

    enviaMensaje(timeStamp)  
    
    pir.wait_for_no_motion()
    print("todo en calma!")
    