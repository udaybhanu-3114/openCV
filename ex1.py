import cv2
import time
img = cv2.imread('uday.jpg')
cv2.imwrite('my_picCopy.jpg',img)
cv2.imshow('my_img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()