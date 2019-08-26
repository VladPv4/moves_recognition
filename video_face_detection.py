import cv2, time

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video=cv2.VideoCapture(0)
a=0

while True:
    a=a+1
    check, frame = video.read() 
    faces=face_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    resized = cv2.resize(frame,(int(frame.shape[1]/3),int(frame.shape[0]/3)))
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow('Video Live',resized)
    key=cv2.waitKey(1)
    if key==ord('q'):
        cv2.imwrite(str('frames'+ str(a) + 'q.jpg'),frame)
        break

        
print(a)
video.release()
cv2.destroyAllWindows
