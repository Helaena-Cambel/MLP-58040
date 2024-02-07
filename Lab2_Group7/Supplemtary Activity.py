import cv2 as cv

def record():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter('andrey.mp4', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('Recording', frame)
        out.write(frame)
        if cv.waitKey(1) == ord('q'):
            out.release()
            print("Recording stopped.")
            break
    cap.release()
    cv.destroyAllWindows()

def play():
    cap = cv.VideoCapture('andrey.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('Playback', frame)
        if cv.waitKey(12) == ord('p'):
            break
    cap.release()
    cv.destroyAllWindows()

while True:
    print("Press 1 to record")
    print("Press 2 to play")
    print("Press q to quit")
    choice = input('Enter your choice: ')

    if choice == '1':
        record()
    elif choice == '2':
        play()
    elif choice == 'q':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
