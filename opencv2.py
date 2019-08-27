import cv2 as c
import numpy as np

img=c.imread('download.jpeg') #reading the image
c.imshow('ISI AGENT ',img) #displaying the image
c.waitKey(0) #wait key, to hold until something is pressed
def ImgRGB():
    #------------------
    #distributing the image into RGB seperately 
    blue,green,red=c.split(img) #returns values in BGR instead of RGB
    print(blue,green,red,sep='\n')
    print(blue.shape,type(blue)) #type is ndarray , having 224 rows and 225 cols
    #------------
    #displaying both seperately

    zeros=np.zeros((img.shape[:2]),dtype=np.uint8) #passing shape (224,225) instead of (224,225,3) 
    #bc 3 is total colors, which is RGB, and we need only rows and cols
    c.imshow('BLUE',c.merge([blue,zeros,zeros]))
    c.imshow('GREEN',c.merge([zeros,green,zeros]))
    c.imshow('RED',c.merge([zeros,zeros,red]))
    c.waitKey(0)
    c.waitkey(0)

def IMGDISTR():
    row,col=img.shape[:2]
    '''
    Translating the image using the matrix
    T = [[1 0 Tx]
         [0 1 Ty]]
    '''
    T = np.float32([[1, 0 ,row/4],[0 , 1 , row/4]])
    Timg=c.warpAffine(img,T,(row,col))
    c.imshow("Translated Image",Timg)
    c.waitKey(0)
IMGDISTR()
