import cv2, os

originalImage = cv2.imread('Introduction to OpenCV\pika.png')

cv2.imshow('Pikachu', originalImage)
cv2.waitKey(0)

greyscaledImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscaled Pikachu', greyscaledImage)

#Saving the Greyscaled Image
#cv2.imwrite('greyscaledPikachu.png', greyscaledImage)
#cv2.imwrite('Images\opencv-assets-main\Greyscaled Pikachu.png', greyscaledImage)

#Storing our to a differnt directory
os.chdir('C:/Users/aryan/OneDrive/Desktop/DUMMY')
cv2.imwrite('greyscaledPikachu.png', greyscaledImage)
print('Successfully Saved Image')

cv2.waitKey(0)

cv2.destroyAllWindows()