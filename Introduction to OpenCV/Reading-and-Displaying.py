import cv2

#Reading the Image
originalImage = cv2.imread('Introduction to OpenCV\Capt-America.jpg')

#Displaying the Image
cv2.imshow('Captain America', originalImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
