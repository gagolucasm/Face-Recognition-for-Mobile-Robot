
###############################################################
###############################################################
########
########    Adquisicion de imagen de Asus Xtion usando ROS
########                   Version 0.1
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
recognizer = cv2.face.createLBPHFaceRecognizer()
et = libs.EyeTracker("cascades/haarcascade_frontalface_alt2.xml")
i=0
path = 'faces'
#print  time.time() - start_time
images,labels,dictid=libs.read_data(path)
print labels
recognizer.train(images, np.array(labels))

class image_converter:
    def __init__(self):

    	self.bridge = CvBridge()
    	self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)

    def callback(self,data):
	i=0
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
                    if conf < 70:
                        print "Reconozco a {} con una confianza de {}".format(
                            (list(dictid.keys())[list(dictid.values()).index(pred)]), conf)
                    else:
                        print "Desconocido"
            cv2.imshow("Tracking", frame)
	    print 'hola'
            cv2.waitKey(50)
        except CvBridgeError as e:
            print(e)



ic = image_converter()


rospy.init_node('image_converter', anonymous=True)

try:
	rospy.spin()
except KeyboardInterrupt:
	print("Cerrando")
	cv2.destroyAllWindows()


