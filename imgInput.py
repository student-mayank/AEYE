import cv2


def imgInput():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(1)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Capture a frame
    ret, frame = cap.read()

    # Check if the frame is not empty
    if not ret:
        print("Cannot capture frame")
        exit()
    # return frame

    cv2.imwrite("img.png", frame) 
    

    
    