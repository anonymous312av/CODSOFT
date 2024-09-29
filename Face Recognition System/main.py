import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

face_match = False
reference_img = cv2.imread("Me.jpg")

lock = threading.Lock()
running_thread = None
no_face_counter = 0  
NO_FACE_THRESHOLD = 10  

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def check_face(face_region):
    global face_match
    try:
        result = DeepFace.verify(face_region, reference_img.copy(), model_name='Dlib')['verified']
        with lock:
            face_match = result
    except ValueError:
        with lock:
            face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            no_face_counter = 0  

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face_region = frame[y:y + h, x:x + w]

                if running_thread is None:  
                    running_thread = threading.Thread(target=check_face, args=(face_region,))
                    running_thread.start()

            with lock:
                if face_match:
                    cv2.putText(frame, "Face Match!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                else:
                    cv2.putText(frame, "No Match!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        else:
            no_face_counter += 1
            if no_face_counter > NO_FACE_THRESHOLD:
                with lock:
                    face_match = False 

        cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
