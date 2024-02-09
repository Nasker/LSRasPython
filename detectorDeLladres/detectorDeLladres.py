import os
import datetime
import http.client, urllib
from gpiozero import MotionSensor 
import pygame.camera

pirPin = 16

width = 640
height = 480

pir = MotionSensor(pirPin)


def enviaMensaje(mensaje):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "awq42rfkakrn9t9v3rak1jc1wg9po8", #YOUR TOKEN
    "user": "unzod5y5ynqjrdywft5i1x9bxqtibf",  #YOUR USER
    "message": mensaje, 
  }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.set_caption('Camera')

while True:
    print("Buscando movimiento...")
    pir.wait_for_motion()
    print("Movimiento detectado!")
    print("Realitzando captura de imagen!")
    image = cam.get_image()
    
    windowSurfaceObj.blit(image,(0,0))
    pygame.display.update()
    
    now = datetime.datetime.now()
    timeStamp = str(now.strftime("%Y-%m-%d_%H:%M:%S"))
    fileName = "Captura"+timeStamp+".jpg"
    print("Guardando imagen con nombre: " + fileName)
    pygame.image.save(image,fileName)
    
    enviaMensaje(timeStamp)  
    
    pir.wait_for_no_motion()
    print("todo en calma!")
    