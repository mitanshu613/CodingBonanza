import cv2
import numpy as np
import os

# Specify the path to the custom background image
background_image_path = 'bg.jpg'

# Check if the background image file exists
if not os.path.isfile(background_image_path):
    print(f"Error: The file '{background_image_path}' does not exist.")
    exit()

# Load the custom background image
background_image = cv2.imread(background_image_path)

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the custom background to match the frame size
    background_image = cv2.resize(background_image, (frame.shape[1], frame.shape[0]))

    # Convert the frame to grayscale for better masking
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create a mask of the background by thresholding the grayscale frame
    _, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract the foreground and background regions
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    background = cv2.bitwise_and(background_image, background_image, mask=mask)

    # Combine the foreground and background to get the result
    result = cv2.add(foreground, background)

    cv2.imshow("Background Replacement", result)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
