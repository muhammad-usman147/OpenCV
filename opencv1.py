import cv2
def NormalImage():
    img=cv2.imread('flower.jpeg') #reading the image
    cv2.imshow('output image',img) #showing the read images
    print(img.shape) #it shows three outputs. height width, and numbers of color, which is 3 Red, Green, Blue (rgb)
    print('height of the images is '+str(img.shape[0]))
    print('width of the image is '+str(img.shape[1]))
    cv2.waitKey(0) #hold the output
#--------------
#converting the grey Scale images into GreyScale
def GreyScale():
    img=cv2.imread('butterfly.jpg')
    cv2.imshow('Normal Image',img)
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Converted Grey Scale image",grey_img)
    cv2.waitKey(0)

GreyScale()
cv2.destroyAllWindows()