# 1. Read and show vide stream, captures images.
# 2. Detect faces and show bounding box
# 3. Flatten the larges face image and save in numpy array
# 4. Repeat this on multiple peoople to generate training data

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

skip = 0
face_list = []
dataset_path = './data/'
file_name = input("Enter the name of the person : ")

while True:

    ret,frame = cap.read()
    if ret == False:
        continue

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame,1.3,5)
    faces = sorted(faces,key = lambda f: f[2]*f[3],reverse=True)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        offset = 10
        face_section = gray_frame[y-offset:y+h+offset,x-offset:x+w+offset]
        if face_section is not None:
            face_section = cv2.resize(face_section,(100,100))

        cv2.imshow("Face Section", face_section)

        skip+=1
        if skip%3 == 0:
            face_list.append(face_section)
            print(len(face_list))
        
    cv2.imshow("Captured frames",frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break


face_list = np.array(face_list)
face_list = face_list.reshape((face_list.shape[0],-1))
np.save(dataset_path+file_name+'.npy',face_list)

cap.release()
cv2.destroyAllWindows()
