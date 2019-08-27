import cv2 as c
img = c.imread('download.jpeg')
c.imshow('image',img)
def RotateImage():
    h,w = img.shape[:2]
    rotater = c.getRotationMatrix2D((h/2,w/2),90,.8)
    rotated_image=c.warpAffine(img,rotater,(h,w))
    c.imshow('Rotated Image',rotated_image)
    c.waitKey(0)
    c.destroyAllWindows()
RotateImage()