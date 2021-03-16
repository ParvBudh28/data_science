# Read a Video Stream from Camera (Frame by Frame)
import cv2

# 0 passed above basically denotes default webcam 
# if we have multiple webcams then we can experiment with different ids
cap = cv2.VideoCapture(0)

while True:

    # ret -> bool value
    # frame is the image captured
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # if ret is false then image not captured properly
    if ret == False:
        continue

    # displaying the image
    cv2.imshow("Video Frame",frame)
    cv2.imshow("Gray Frame",gray_frame)

    # Wait for user input
    # -q,then we stop the loop
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

    # When we use waitKey(0) - then the program stops when any key is pressed

cap.release()
cv2.destroyAllWindows()