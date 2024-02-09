#!/usr/bin/python
import pygame.camera

width = 640
height = 480

pygame.camera.init()
camlist = pygame.camera.list_cameras()
print (camlist)

cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

windowSurfaceObj = pygame.display.set_mode((width,height))
pygame.display.set_caption('Camera')

while True:
    image = cam.get_image()
    windowSurfaceObj.blit(image,(0,0))
    pygame.display.update() 