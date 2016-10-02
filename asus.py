
###############################################################
###############################################################
########
########    Demo con el robot para presentacion del TFG
########                   Version 0.2
########                 TFG Lucas Gago
########
###############################################################
###############################################################

## roslaunch openni2_launch openni2.launch


__author__ = 'lucasgago'

## Importamos las librerias necesarias
import roslib
import sys
import numpy as np
import rospy
import time
import cv2
import libs
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pyttsx
import speech_recognition as spr


## Definimos la clase para convertir la imagen al formato
## necesario para trabajar en opencv con ella
class image_converter:
    
    ## Funcion que se ejecuta con la creacion de la clase
    def __init__(self):
	
    	global et
	global recognizer
	global dictid, labels
        self.engine1 = pyttsx.init()
	self.engine = pyttsx.init()
	self.engine1.say('Initializing components.         All systems ready.')
        self.engine1.runAndWait()
    	self.bridge = CvBridge()
    	self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)
	recognizer = cv2.face.createLBPHFaceRecognizer()
	et = libs.EyeTracker("cascades/haarcascade_frontalface_alt2.xml")
	i=0
	path = 'faces'
	images,labels,dictid=libs.read_data(path)
	print labels
	recognizer.train(images, np.array(labels))
	print 'termine'
	self.num=0

    def callback(self,data):
        i=0
	rg=spr.Recognizer()
        try:
            frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
            frame = libs.resize(frame, width=600)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            (rects, i, facess) = et.track(gray, i)
            for rect in rects:
                cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
            if facess != []:
                for face in facess:
                    pred, conf = recognizer.predict(face)
                    if conf < 120:
                        print "Reconozco a Lucas con una confianza de {}".format(conf)
			self.num=self.num+1
			if self.num==10:
                        	self.engine.say('Hi ')
				#self.engine.say( list(dictid.keys())[list(dictid.values()).index(pred)])
				self.engine.say('Lucas')
				self.engine.runAndWait()
				with spr.Microphone() as source:
					rg.adjust_for_ambient_noise(source)
					print 'Escuchando'
					audio=rg.listen(source)
					try:
						respuesta= rg.recognize_sphinx(audio)
						print respuesta
						if respuesta!='no':
							self.engine.say('OKEY ')
							self.engine.say('Getting')
							self.engine.say('new')
							self.engine.say('data')
							self.engine.runAndWait()
					except spr.UnknownValueError:
						print 'error'
				
                    else:
                        print "Desconocido"
            cv2.imshow("Tracking", frame)
            cv2.waitKey(1)
        except CvBridgeError as e:
            print(e)



ic = image_converter()
rospy.init_node('image_converter', anonymous=True)
try:
	rospy.spin()
except KeyboardInterrupt:
	print("Cerrando")
	cv2.destroyAllWindows()


