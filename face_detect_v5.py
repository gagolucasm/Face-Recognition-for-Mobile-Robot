__author__ = 'lucasgago'

import cv2
import numpy as np
import time
import libs
start_time = time.time()
#Para raspberry
#from picamera.array import PiRGBArray
#from picamera import PiCamera

#camera = PiCamera()
#camera.resolution = tuple(1024)
#camera.framerate = 30
#rawCapture = PiRGBArray(camera, size=tuple(1024))
recognizer = cv2.face.createLBPHFaceRecognizer()

et = libs.EyeTracker("cascades/haarcascade_frontalface_alt2.xml")

camera = cv2.VideoCapture(0)
#for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
i=0
path = 'faces'
print  time.time() - start_time
images,labels,dictid=libs.read_data(path)
print labels
recognizer.train(images, np.array(labels))
while(True):
    #frame = f.array
    (grabbed, frame) = camera.read()
    frame = libs.resize(frame, width = 600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (rects,i,facess) = et.track(gray,i)
    for rect in rects:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
    if facess!=[]:
        for face in facess:
            pred, conf = recognizer.predict(face)
            if conf<70:
                print "Reconozco a {} con una confianza de {}".format((list(dictid.keys())[list(dictid.values()).index(pred)]), conf)
            else:
                print "Desconocido"
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()

