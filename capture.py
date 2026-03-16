import cv2
cap = cv2.VideoCapture(0)  # 0 is de standaard webcam

while True:
    ret, frame = cap.read()

    # Toon de live beelden
    cv2.imshow('Webcam Feed', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Feed', gray)

    # Stop als de gebruiker op 'q' drukt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
