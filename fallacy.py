import cv2
from ultralytics import YOLO

model = YOLO("Path to the model")
cam = "http://192.168.137.197:8080/video" #IP webcam link
cap = cv2.VideoCapture(0)
cap.open(cam)
print("check ===>", cap.isOpened())

while cap.isOpened():
    success, frame = cap.read()

    if success:
        frame = cv2.resize(frame, (700, 700))
        results = model(frame)
        for det in results:
            # Assuming det is the class label (e.g., "rotten")
            cls = det
            # cv2.putText(frame, f"{cls}({conf:.2f})", (int(x_min), int(y_min) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
            #             (255, 0, 0), 2)
        cv2.imshow("WebCam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
