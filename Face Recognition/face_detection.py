# Face Detection using HaarCascade classifier and Open CV
# This is an older method
# Now a days we use CNN


# Read a Video Stream from Camera (Frame by Frame)
import cv2

# 0 passed above basically denotes default webcam 
# if we have multiple webcams then we can experiment with different ids
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:

    # ret -> bool value
    # frame is the image captured
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # if ret is false then image not captured properly
    if ret == False:
        continue

    # scaleFactor - how much image size is reduced in each try 
    # works upon fixed size of image therefore needs scaling
    # no of neighbours - 3-6 is good given in documentation
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)

    # faces returns the coordinates of the face
    # drawing rectangle around the faces detected
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # displaying the image
    cv2.imshow("Video Frame",frame)

    # Wait for user input
    # -q,then we stop the loop
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

    # When we use waitKey(0) - then the program stops when any key is pressed

cap.release()
cv2.destroyAllWindows()
