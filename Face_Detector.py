import cv2
from random import randrange

# open Cv detects from top left to right

# load some pre-defined data from open cv (haar cascade algo)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose img to detect faces

# img = cv2.imread('rdj.jpeg')

# to capture video from web cam

# 0 for opening ur default webcam
webcam=cv2.VideoCapture(0)
# key=cv2.waitKey(1)

# iterate forever over frames
while True:
   # read the current frame wether read or not and returns True or False and also return the current frame (image)
    successful_frame_read, frame = webcam.read() 
    greyscaled_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_frame)
    for x,y,w,h in face_coordinates:
        cv2.rectangle(frame, (x,y) ,(x+w, y+h), (0,255,0),2)
    cv2.imshow("Face Detector", frame)
    key=cv2.waitKey(1)

    # if q is pressed then it will quit ( q or Q in ascii)

    if key==81 or key==113:
        break

# Release the video captured by object
webcam.release()


# must convert to gray scale coz haar algo uses greay scale images
# in open cv the channels are reverse that is BGR Not RGB
# greyscaled_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# can convert back from gray to RGB but once you lose the color, it will still show greay though considered grey

# abc=cv2.cvtColor(greyscaled_frame,cv2.COLOR_BayerRG2BGR)

# Detect Faces

# gives coordinate of upper left corner and width and height of square
# face_coordinates = trained_face_data.detectMultiScale(greyscaled_frame)
# print(face_coordinates)

# Draw rectangles around faces

# cv2.rectangle(frame, (352,135 ) ,(325+474, 135+474), (255,0,0), 2)

# to detect multiple faces in a pic
# for x,y,w,h in face_coordinates:
#     cv2.rectangle(frame, (x,y) ,(x+w, y+h), (randrange(256),randrange(256),randrange(256)),10)

# Displaying images with faces

# open and instantly closes
# cv2.imshow("Face Detector", frame)

# pauses the execution of code until a key is pressed
# cv2.waitKey()

# print("Code completed")

