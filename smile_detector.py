import cv2
import numpy as np

i = 0
def detect_faces_and_smiles(frame: np.ndarray)-> np.ndarray:
    classifier = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    coord = classifier.detectMultiScale(frame_gray, 1.1, 30)

    faces = []
    for x, y, w, h in coord:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)        
        faces.append(frame[y:y+h, x:x+w])
    
    global i
    for face in faces:
        detected = detect_smiles(face)
        ## the second evaluation is to reduce the number of images saved
        if detected:
            name = f"smile_{i}.jpg"
            if (i == 0 or i%5 ==0):
                cv2.imwrite(name, frame)
            i+=1

    return frame

def detect_smiles(frame: np.ndarray)-> bool:
    classifier = cv2.CascadeClassifier("haarcascades/haarcascade_smile.xml")
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # obs: needed to put the detection strictness really high
        #  because due to my resting face, the algorithm always thinks im smiling
    coord = classifier.detectMultiScale(frame_gray, 1.1, 100)

    for x, y, w, h in coord:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
      
    return len(coord) > 0
    
# # # # # # # Main # # # # # # # 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    output = detect_faces_and_smiles(frame)
    cv2.imshow("smile detection", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()