import cv2
image = cv2.imread('uday.jpg')
greyImg = cv2.cvtColor(image,cv2.COLOR_BGR2LUV)
cv2.imwrite('Luv_image.jpg',greyImg)
cv2.imshow('color_image',image)
cv2.imshow('Luv_image',greyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()