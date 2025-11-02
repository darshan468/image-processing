import cv2  #library for image processing

img = cv2.imread("pandya.jpg") #reading the image
cv2.imwrite("pandya.jpg",img)  #writing the image
cv2.imshow("Rising Star",img)  #displaying the image
cv2.waitKey(0) 
cv2.destroyAllWindows()