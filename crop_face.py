import cv2

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
i=0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 7)
    for (x,y,w,h) in faces:
	        #print(w*h)
	        #if w*h > 6500:
	    
	    # cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
	    cv2.imwrite('Arpit'+str(i)+'.jpeg', img_sv)
	    i+=1
	    cv2.putText(img, str(i) ,(x,y-10), font, .5,(255,255,255),2,cv2.CV_AA)
    cv2.imshow('Image', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
	