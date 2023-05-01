import cv2
import paths

car_cascade = cv2.CascadeClassifier(paths.CASCADE_PATH)

# set the camera for cv2 to capture from (index 0 as I don't use more than one USB camera)
cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
        # perform operations on the frame (e.g., display, process, etc.)
        cv2.imshow('Webcam Feed', frame)
        
        # break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()  