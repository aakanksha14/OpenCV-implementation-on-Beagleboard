# Lab 4 - Computer Vision
# Aakanksha Mathuria
# 27 Feb 2019

# Importing packages
import numpy as np
import cv2

# Adapted from https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

# Capturing video
#VideoStream = cv2.VideoCapture(0)
VideoStream = cv2.VideoCapture("drop.avi")

# Check if camera opened successfully
if (VideoStream.isOpened()== False): 
  print("Error opening video stream or file")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(VideoStream.get(3))
frame_height = int(VideoStream.get(4))

print(frame_width)
print(frame_height)

# Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.

#out = cv2.VideoWriter('output.AVI',cv2.VideoWriter_fourcc('M','J','P','G'), 20, (frame_width,frame_height), 0)
# out2 = cv2.VideoWriter('output2.AVI',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height), 0)
Writer_cannyEdge = cv2.VideoWriter('CannyEdge.avi',cv2.VideoWriter_fourcc(*'DIVX'), 20, (frame_width,frame_height), 0)
Writer_trackFeatures = cv2.VideoWriter('TrackFeatures.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, (frame_width,frame_height), 0)

# Read until video is completed
while(VideoStream.isOpened()):
  # Capture frame-by-frame
  ret, frame = VideoStream.read()
  if ret == True:

    # Modifying the video's resolution
    #ret = VideoStream.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    #ret = VideoStream.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

    # frame_width = int(VideoStream.get(3))
    # frame_height = int(VideoStream.get(4))
    # print(frame_width)
    # print(frame_height)

    # Converting to monochrome
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Gray frame', gray)

    # Canny edge detection
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Canny edges', edges)

    # Write canny edge detection result to the file
    Writer_cannyEdge.write(edges)

    # goodFeaturesToTrack to identify and track features in the video
    corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)

    for i in corners:
    	x,y = i.ravel()
    	cv2.circle(gray,(x,y),3,255,-1)

    # Display the resulting frame - track features
    cv2.imshow('Track features', gray)

    # Write identified features to the file
    Writer_trackFeatures.write(gray)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object and video writers
VideoStream.release()
Writer_cannyEdge.release()
Writer_trackFeatures.release()
 
# Closes all the frames
cv2.destroyAllWindows()