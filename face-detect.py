import numpy as np
import cv2,thread,time
import tkinter as tk
import tkMessageBox
stop = False
def gui():
	root = tk.Tk()
	tkMessageBox.showinfo('', 'Image Detected')
	
	#time.sleep(2)
	

cam = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
while True:
    ret,frame = cam.read()

    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # print(faces)
    if faces != ():
    	thread.start_new_thread(gui, ())
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()
