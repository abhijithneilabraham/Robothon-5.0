#Coordinates 
import cv2 #importing the opencv module

video_capture = cv2.VideoCapture(0) #videocapture for starting to capture video
i=0
while True:
    video_capture.grab()
    retrival, frame = video_capture.retrieve(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"Elevation  : "+str(25),(10,450), font, 1,(0,255,0),2,cv2.LINE_AA)
    X=9.3172012081
    Y=76.6780318411
    Lat=(X+(0.0000000001*((i*1213)%171)))
    Lng=(Y+(0.0000000001*((i*1297)%137)))
    cv2.putText(frame,"Latitude   : "+str(Lat),(10,420), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(frame,"Longitude : "+str(Lng),(10,390), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to exit the capture mode
        break
    i+=1
    

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
