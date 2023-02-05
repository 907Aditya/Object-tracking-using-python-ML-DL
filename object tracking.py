 
import cv2 # import opencv


cap = cv2.VideoCapture(0) # capture the vid

#tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.legacy.TrackerCSRT_create()  #tracter for tracking the object 

success, img = cap.read() # read the image
bbox = cv2.selectROI("Tacking",img,False)#to create a bounding box 
tracker.init(img,bbox)#initialing our tracker
def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 3)




while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    success,bbox = tracker.update(img)
    print(bbox)
    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, "Lost",(75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer) #to calculat the fps
    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),3)# to put fps on vid
    cv2.imshow("Tracking",img) # show the image as tracking 
    if cv2.waitKey(1) & 0xff == ord('q'):# to close
        break 

