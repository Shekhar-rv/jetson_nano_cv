from sre_constants import SUCCESS
import cv2
# print(cv2.__version__)

# ### Importing an image
# # Point to the image file
# img = cv2.imread('resources/download.jpeg')
# # Select the windwe and image to be displayed
# cv2.imshow('Output', img)
# # Set a delay time to infinity
# cv2.waitKey(0)

### Importing a video
# Set the width and height of the video
# frameWidth = 640
# frameHeight = 480
# # Point to the video file
# cap = cv2.VideoCapture('resources/test_video.mp4')

# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     # Show the video
#     cv2.imshow('Result', img)
#     # Break the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

### Running a webcam
# Set the width and height of the video
frameWidth = 640
frameHeight = 480
# Point to the webcam file - 
cap = cv2.VideoCapture("nvarguscamerasrc ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink", cv2.CAP_GSTREAMER)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    # Show the video
    cv2.imshow('Result', img)
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break