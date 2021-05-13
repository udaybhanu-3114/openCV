import cv2
image = cv2.imread('uday.jpg')
greyImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg',greyImg)
cv2.imshow('color_image',image)
cv2.imshow('Grey_image',greyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()