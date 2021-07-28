#!/usr/bin/python3
import os 
os.system("pip3 install  opencv-python && pip3 install cryptography ")
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 32:
        # space pressed to stop
        print("Escape hit, closing...")
        break
    elif k%256 == 27:
        # ESC pressed to screenshot
        img_name = "opencv_frame_{}.png".format(img_counter)

        cv2.imwrite(img_name, frame)
        img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(frame, None, fx=0.5, fy=1, interpolation=cv2.INTER_AREA)
        print('Resized Dimensions : ', img.shape)
        cv2.imwrite("_resized"+img_name, img)
        print("{} written!".format(img_name))
        img_counter += 1
        
cam.release()
