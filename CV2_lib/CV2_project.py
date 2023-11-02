#this python program displays image in (colour"1"/gray"0") by using CV2 library
import numpy as np
import cv2
from time import sleep

print ("Project - Below program loads an image in grayscale, displays it, save the image if you press ‘s’ and exit, ")
print (" or simply exit without saving if you press ESC key.")
sleep(1)


img = cv2.imread('flower.jpg',1)
print(img)
cv2.imshow( "Input Image", img )
print ("1st print done",'\n')


img1 = cv2.imread('flower.jpg',0)
print(img1)
cv2.imshow("Gray Image",img1)

while(True):
 k = cv2.waitKey(0)
 if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    break

 elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('Output Image Store.jpg',img1)
    cv2.destroyAllWindows()
    break


print ("Project end")
