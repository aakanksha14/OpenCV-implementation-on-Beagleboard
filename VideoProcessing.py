# Lab 4 - Computer Vision
# Aakanksha Mathuria
# 27 Feb 2019

# Importing packages
import numpy as np
import cv2

# Adapted from https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

# Capturing video
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("MVI_4184.AVI")

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

print(frame_width)
print(frame_height)

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Modifying the video's resolution
    ret = cap.set(3,1280)
    ret = cap.set(4,1024)

    # Converting to monochrome
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Frame', gray)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()