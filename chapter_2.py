import cv2
import numpy as np

# The are the basics of image processing with OpenCV

# Load an image
img=cv2.imread("resources/download.jpeg")
# Conver to grayscale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Blur the image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
# Edge detection
imgCanny=cv2.Canny(imgBlur,150,250)
# Define the kernel and dilate the image 
kernel=np.ones((5,5),np.uint8)
imgDia = cv2.dilate(imgCanny, kernel, iterations=1)
# Erode the image
imgErode = cv2.erode(imgDia, kernel, iterations=1)

# Show the images
cv2.imshow("Output",img)
cv2.imshow("Output",imgGray)
cv2.imshow("Output",imgBlur)
cv2.imshow("Output",imgCanny)
cv2.imshow("Output",imgDia)
cv2.imshow("Output",imgErode)
# Wait for a key press
cv2.waitKey(0)