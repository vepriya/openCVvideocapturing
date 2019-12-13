import numpy as np
import os
import cv2


filename = 'video.avi'  ##file name in which captured video will be saved in our working directory
#.avi / .mp4 is extensions for video file , you can choose anyone according to codecs installed in your system
frames_per_second = 24.0
res = '1080p'

# Set resolution for the video capture (to make sure everything is going good)
def change_resolution(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes
STANDARD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STANDARD_DIMENSIONS["480p"]
    if res in STANDARD_DIMENSIONS:
        width,height = STANDARD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_resolution(cap, width, height)
    return width, height

# Video Encoding, might require additional installs according to the codecs of your systems
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']



cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

while True:
    ret, frame = cap.read()
    out.write(frame)   ##write frames in filenmae you provided
    cv2.imshow('frame',frame) ##show the frames on your monitor while capturing 
    if cv2.waitKey(1) & 0xFF == ord('q'):    ##press "q" to stop capturing
        break


cap.release()
out.release()
cv2.destroyAllWindows()
