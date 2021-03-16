# Recognise faces using some classification - KNN


# 1. load the training data (numpy arrays of all the persons)
    # x - values are stored in the numpy arrays
    # y - values we need to assign for each person
# 2. Read a video stream using opencv
# 3. extract faces out of it
# 4. use knn to find the predicition of the face (int)
# 5. map the predictedid to the name of the user
# 6. display the predictions on the screen - bounding box and name

import numpy as np
import cv2
import os

# ------------------- k - NN algo start -------------------------

def dist(x1,x2):
    return np.sqrt(sum((x1-x2)**2))

def knn(X,Y,query_point,k=10):
    
    vals = []
    m = X.shape[0]

    for i in range(m):
        d = dist(X[i],query_point)
        vals.append((d,Y[i]))
    
    vals = sorted(vals,key= lambda x:x[0])[:k]
    vals = np.array(vals)

    new_vals = np.unique(vals[:,1],return_counts=True)
    index = new_vals[1].argmax()

    return new_vals[0][index]

# ------------------- Data Preparation -------------------------
dataset_path = './data/'

face_data = []
labels = []

class_id = 0    # labels for a given file
names = {}  # mapping btw id and name

# Data preparation
for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        names[class_id] = fx[:-4]
        data_item = np.load(dataset_path+fx)
        face_data.append(data_item)
        target = class_id*np.ones((data_item.shape[0],))
        class_id+=1
        labels.append(target)

face_data = np.concatenate(face_data,axis=0)
labels = np.concatenate(labels,axis=0)

# ------------------- Video Capture -------------------------

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,frame = cap.read()
    if ret==False:
        continue

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for face in faces:
        x,y,w,h = face

        offset = 10
        face_section = gray_frame[x-offset:x+w+offset,y-offset:y+h+offset]
        if face_section is not None:
            face_section = cv2.resize(face_section,(100,100))

        face_section = np.array(face_section).reshape((-1,))
        out = knn(face_data,labels,face_section)

        cv2.putText(frame,names[int(out)],(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Faces", frame)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
