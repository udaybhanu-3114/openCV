import cv2
import imutils

img = cv2.imread('uday.jpg')
resizeImg = imutils.resize(img,width=5000)
cv2.imwrite('resizedImage.jpg',resizeImg)