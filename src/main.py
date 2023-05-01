import cv2

cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, frame = cap.read()
        
        # perform operations on the frame (e.g., display, process, etc.)
        cv2.imshow('Webcam Feed', frame)
        
        # break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()  