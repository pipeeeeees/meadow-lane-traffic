import cv2
import os
import shutil
import paths
import datetime

# haarcascade models to detect the shapes and sizes of cars, people
car_haarcascade = cv2.CascadeClassifier(paths.HAARCASCADE_CAR_XML_PATH)
human_haarcascade = cv2.CascadeClassifier(paths.HAARCASCADE_HUMAN_XML_PATH)

# set the camera for cv2 to capture from (index 0 as I don't use more than one USB camera)
cap = cv2.VideoCapture(0)

os.makedirs('src/captures', exist_ok=True)

def adjust_brightness_contrast(image, alpha=1.0, beta=0.0):
    """
    Adjusts the brightness and contrast of an image using alpha and beta parameters.
    alpha > 1.0 increases contrast, 0.0 < alpha < 1.0 decreases contrast.
    beta > 0.0 increases brightness, beta < 0.0 decreases brightness.
    """
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image

def main():
    # empty the 'captures' folder before each run
    shutil.rmtree('src/captures')
    os.makedirs('src/captures', exist_ok=True)

    while True:
        ret, frame = cap.read()

        #frame = adjust_brightness_contrast(frame, alpha=1, beta=0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect cars
        cars = car_haarcascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            label = 'Car'
            cv2.putText(frame, f'{label}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            cv2.imwrite(f'src/captures/car_{x}-{y}_{timestamp}.jpg', frame)

        # detect people
        humans = human_haarcascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in humans:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            label = 'Human'
            cv2.putText(frame, f'{label}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            cv2.imwrite(f'src/captures/human_{x}-{y}_{timestamp}.jpg', frame)

        # perform operations on the frame (e.g., display, process, etc.)
        cv2.imshow('Webcam Feed', frame)
        
        # break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()  