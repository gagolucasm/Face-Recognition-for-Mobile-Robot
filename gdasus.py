

###############################################################
###############################################################
########
########    Software para generacion de base de datos
########                 Version 0.3 PC
########      Comentada la adaptacion a Raspberry Pi
########                 TFG Lucas Gago
########
###############################################################
###############################################################

__author__ = 'lucasgago'

## Importamos las librerias

import cv2
import numpy as np
import time
import os
import libs # Libreria propia con funciones y clases necesarias

## Para Raspberry Pi
#from picamera.array import PiRGBArray
#from picamera import PiCamera
#camera = PiCamera()
#camera.resolution = (1024,768)
#camera.framerate = 30
#rawCapture = PiRGBArray(camera, size=(1024,768))

## Limpiamos el terminal
os.system('cls' if os.name == 'nt' else 'clear')

## Mostramos por pantalla las instrucciones y condiciones
print ""
print "#####################################################"
print "################  TFG Lucas Gago  ###################"
print "################    Version 0.3   ###################"
print "#####################################################"
print ""
print "Hola, si quiere participar en el TFG de Lucas Gago, "
print "escriba su nombre y pulse enter. De esta manera da"
print "permiso para el uso de las imagenes que se capturaran "
print "a continuacion con fines puramente academicos."
print ""
nombre = raw_input('Por favor, escriba su nombre: ')

##_Empezamos la captura de frames
camera = cv2.VideoCapture(0)

## Para Raspberry Pi
#for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

## Iniciamos variables necesarias
i=0
neg = np.zeros((437,700,3), np.uint8)
foto=columna=fila=0
size=100
img = np.zeros((1000,700), np.uint8)

##_Generamos la ventana que almacenara las fotos
cv2.namedWindow('GUI')
xmar=ymar=50
cv2.imshow('GUI',img)

## Empezamos el bucle, termina cuando se hayan capturado 24 imagenes
while(foto<24):
    
    ## para Raspberry Pi
    #frame = f.array

    ## Leemos la imagen de la camara
    (grabbed, frame) = camera.read()
    
    ## Reducimos su tamano para mejorar el rendimiento
    frame = libs.resize(frame, width = 600)
    
    ##_Se convierte a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ## Buscamos rostros en ella
    (rects,i,facess) = ft.track(gray,i)

    ## Si encontramos un rosto, lo guardamos en otra variable
    if (facee!=[]):
        face=facee
    
    ## Si el usuario presiona la tecla F, guardamos la foto actual
    if cv2.waitKey(1) & 0xFF == ord("f") :
        
        ## Aumentamos la cuenta de fotos guardadas
        foto+=1
        
        ## La procesamos dandole un tamano unificado necesario para el
        ## correcto procesamiento en el entrenamiento del sistema de
        ## clasificacion
        img1 = face
        img1=libs.resize(img1,width = size,height=size)
        
        ## Mostramos la foto en el lugar correcto dentro de la ventana de
        ## fotos ya tomadas
        img[ymar+150*fila:ymar+150*fila+img1.shape[0], xmar+(columna*(size+xmar)):xmar+(columna*(size+xmar)+img1.shape[1])] = img1
        
        ## Mostramos instrucciones en pantalla en todo momento
        cv2.putText(img, "Presiona Q para salir", (5, 25),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
        cv2.putText(img, "TFG Lucas Gago", (500, 925),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
        cv2.putText(img, "Version 0.3", (500, 950),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
        cv2.imshow('GUI',img)
        
        ## Guardamos indexando correctamente la imagen actual
        dir="faces/"+nombre+"."+str(i)+".jpeg"
        cv2.imwrite(dir,img1)
        
        ## Avanzamos en fila o columna para mostrar la matriz de imagenes
        if columna<3:
            columna+=1
        else:
            columna=0
            fila+=1

    ## Estamos atentos a la orden del usuario de cerrar la aplicacion
    elif cv2.waitKey(1) & 0xFF == ord("q"):
            break

    ## Dibujamos un rectangulo verde encuadrando los rostros encontrados
    for rect in rects:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
    neg[50:50+frame.shape[0], 50:50+frame.shape[1]] = frame

    ## Mostramos instrucciones por pantalla en la ventana de captura
    cv2.putText(neg, "Presione la tecla F para tomar una foto", (170, 25),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.putText(neg, "TFG L.M.G.", (600, 410),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.putText(neg, "Version 0.3", (600, 430),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.putText(neg, "Tomando datos de "+nombre, (230, 410),cv2.FONT_HERSHEY_SIMPLEX, .6, (255,255,255))
    cv2.imshow("Tracking", neg)
neg = np.zeros((337+100,600+100,3), np.uint8)

## Si ya tomamos las 24 imagenes, agradecemos al usuario su colaboracion
while(foto==24):
    (grabbed, frame) = camera.read()
    frame = resize(frame, width = 600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    neg[50:50+frame.shape[0], 50:50+frame.shape[1]] = frame
    
    ## Mostramos por pantalla las instrucciones
    cv2.putText(neg, "Muchas gracias! Pulse Q para salir del programa.", (150, 25),cv2.FONT_HERSHEY_SIMPLEX, .5, (0,255,0))
    cv2.putText(neg, "TFG L.M.G.", (600, 410),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.putText(neg, "Version 0.3", (600, 430),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.putText(neg, "Tomando datos de "+nombre, (230, 410),cv2.FONT_HERSHEY_SIMPLEX, .6, (255,255,255))
    cv2.imshow("Tracking", neg)
    
    ##_Tambien puede pulsar la tecla Q para salir
    if cv2.waitKey(1) & 0xFF == ord("q"):
            break

## Cerramos el programa
camera.release()
cv2.destroyAllWindows()

## Limpiamos el terminal
os.system('cls' if os.name == 'nt' else 'clear')



