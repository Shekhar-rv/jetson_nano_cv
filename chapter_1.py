import cv2
# print(cv2.__version__)

def load_and_show_image(img_path = "resources/download.jpeg"):
    '''
    This function loads an image and displays it. It takes one argument:
    1. img_path: The path to the image file.
    '''
    ### Importing an image
    # Point to the image file
    img = cv2.imread(img_path)
    # Select the windwe and image to be displayed
    cv2.imshow('Output', img)
    # Set a delay time to infinity
    cv2.waitKey(0)

def load_and_show_video(video_path = "resources/test_video.mp4", frameWidth = 640, frameHeight = 480):
    '''
    This function loads a video and displays it. It takes three arguments:
    1. video_path: The path to the video file.
    2. frameWidth: The width of the video frame.
    3. frameHeight: The height of the video frame.
    '''
    # Point to the video file
    cap = cv2.VideoCapture(video_path)
    while True:
        # success, img = cap.read()
        img = cap.read()[1]
        img = cv2.resize(img, (frameWidth, frameHeight))
        # Show the video
        cv2.imshow('Result', img)
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def load_and_show_webcam(frameWidth = 640, frameHeight = 480):
    '''
    This function loads a webcam and displays it. It takes two arguments:
    1. frameWidth: The width of the video frame.
    2. frameHeight: The height of the video frame.
    '''
    # Point to the webcam file - uncomment first lineif you have a usb webcam
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("nvarguscamerasrc ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink", cv2.CAP_GSTREAMER)

    while True:
        img = cap.read()[1]
        img = cv2.resize(img, (frameWidth, frameHeight))
        # Show the video
        cv2.imshow('Result', img)
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    # Uncomment the function you want to run
    # load_and_show_image()
    # load_and_show_video()
    load_and_show_webcam()