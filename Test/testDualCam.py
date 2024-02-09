#!/usr/bin/python
import pygame.camera

#tamaño de la ventana
width = 640
height = 480

#inicializamos la camara 
pygame.init()
pygame.camera.init()
camlist = pygame.camera.list_cameras()
print (camlist)
cam1 = pygame.camera.Camera("/dev/video0",(320,240))
cam2 = pygame.camera.Camera("/dev/video1",(320,240))
cam1.start()
cam2.start()

#configuramos el tamanyo de la ventana  (comentar en modo de autorranque sin pantalla)
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.set_caption('Camera')

while True:
    #print("Realitzando captura de imagen!")
    image1 = cam1.get_image() #guardamos el frame de la camara en el momento que detectamos movimiento
    image2 = cam2.get_image() 
    #mostramos las imagenes por pantalla (comentar en modo de autoarranque sin pantalla)
    windowSurfaceObj.blit(image1,(0,0))
    windowSurfaceObj.blit(image2,(320,0))
    pygame.display.update() 