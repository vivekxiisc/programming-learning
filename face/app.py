import cv2

# 1. OpenCV ka pre-trained model (Haar Cascade) load karna
# Yeh chehre (faces) ke patterns ko pehchanne mein madad karta hai
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Webcam chalu karna
cap = cv2.VideoCapture(0)

print("--- Face Detection Start Ho Raha Hai ---")
print("Band karne ke liye video window par click karke 'Q' dabayein.")

while True:
    # Webcam se ek frame lena
    ret, frame = cap.read()
    if not ret:
        print("Webcam nahi mil raha!")
        break

    # 3. Image ko Gray (Black & White) mein badalna
    # Computer ke liye B&W image process karna fast hota hai
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 4. Chehre dhoondhna (Detection Logic)
    # scaleFactor: image ko kitna chota karna hai check karne ke liye
    # minNeighbors: kitne boxes ek jagah hone chahiye chehra manne ke liye
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 5. Har mile hue chehre par box aur text lagana
    for (x, y, w, h) in faces:
        # Blue Color ka box (B, G, R) format mein
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        cv2.putText(frame, 'FACE FOUND', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # 6. Live window dikhana
    cv2.imshow('BCA OJT Project - Face Detection', frame)

    # 'Q' dabane par loop break karna
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Sab band karna
cap.release()
cv2.destroyAllWindows()
print("Project Closed Successfully.")