import cv2
import numpy as np
import math

points = []

def drawcircle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(int(x),int(y)),6,(255,0,0),-1)
        if (len(points)!=0):
            cv2.arrowedLine(img,tuple(points[0]),(x,y),(255,0,0),3)
        points.append([x,y])
        cv2.imshow('image',img)
        print(points)
        if (len(points)==3):
            degrees = findangle()
            print(degrees)
    

def findangle():
    a = points[-2]
    b = points[-3]
    c = points[-1]
    m1 = slope(b,a)
    m2 = slope(b,c)
    angle = math.atan((m2-m1)/1+m1*m2)
    angle = round(math.degrees((angle)))
    if angle<0:
        angle = 180 + angle
    cv2.putText(img,str(angle),(b[0]-40,b[1]+40),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),1,cv2.LINE_AA)
    cv2.imshow('image',img)
    return angle

def slope(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

img = cv2.imread(r"C:\Users\sahas\OneDrive\Documents\visual studio code\openCv\projects\images\protractor.jpg")
while True:
    cv2.imshow('image',img)
    cv2.setMouseCallback('image', drawcircle)
    if cv2.waitKey(1) & 0xff==ord('r'):
        img = cv2.imread(r"C:\Users\sahas\OneDrive\Documents\visual studio code\openCv\projects\images\protractor.jpg")
        points=[]
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', drawcircle)
    if cv2.waitKey(1)&0xff==ord('q'):
        break