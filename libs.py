__author__ = 'lucasgago'

import cv2
import os
import numpy as np
import time


class EyeTracker:
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
    def track(self, image,i):
        faceRects = self.faceCascade.detectMultiScale(image,
            scaleFactor = 1.1, minNeighbors = 10,
            minSize = (40, 40), flags = cv2.CASCADE_SCALE_IMAGE )
        rects = []
        faceROI=[]

        for (fX, fY, fW, fH) in faceRects:
            if(i<25):
                i=i+1
            else:
                i=0
            fH=fW
            faceROI.append (image[fY:fY + fH, fX:fX + fW])
            rects.append((fX, fY, fX + fW, fY + fH))
        return rects,i,faceROI


def resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):
    dim = None
    (h, w) = image.shape[:2]
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    if height is None:
        r = width / float(w)
        dim = (width, int(h * r))
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

def gui():
    size=100
    img = np.zeros((1000,700,3), np.uint8)
    cv2.namedWindow('GUI')
    xmar=ymar=50
    for i in range(6):
        for j in range(4):
            img1 = cv2.imread("faces/cara"+str(i+j+1)+".JPEG")
            img1=resize(img1,width = size,height=size)
            if (img1.shape[0] == 100 and img1.shape[1] == 100):
                img[ymar:ymar+size, xmar+(j*(size+xmar)):xmar+(j*(size+xmar)+size)] = img1
            else:
                img[ymar:ymar+img1.shape[0], xmar+(j*(size+xmar)):xmar+(j*(size+xmar)+img1.shape[1])] = img1
        ymar+=150
    cv2.putText(img, "Presiona Q para salir", (5, 25),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.putText(img, "TFG Lucas Gago", (500, 925),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.putText(img, "Version 3", (500, 950),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
    cv2.imshow('GUI',img)

def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))

    return rms

def read_data(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('re')]
    images=[]
    labels=[]
    for image_path in image_paths:
        #print image_path
        #cv2.namedWindow('Cargando fotos ...')
        imagen=cv2.imread(image_path)
        imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagenn=np.array(imagen,'uint8')
        #cv2.imshow("Cargando fotos ...",imagenn)
        #cv2.waitKey(40)
        nbr = (os.path.split(image_path)[1].split(".")[0])
        images.append(imagenn)
        labels.append(nbr)
    id=set(labels)
    #print id
    dictid={}
    pos=0
    idlabel=[]
    for i in id:
        dictid[i]=pos
        pos=pos+1
    for i in labels:
        idlabel.append(dictid[i])
    return images,idlabel,dictid
