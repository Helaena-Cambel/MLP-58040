import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while (True):
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    resized = cv.resize(frame, (240, 180))
    sobel_xy = cv.Sobel(src=resized, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobel_xy)
    canny = cv.Canny(resized, 100, 200)
    laplacian = cv.Laplacian(resized, cv.CV_64F)
    filtered = cv.convertScaleAbs(laplacian)

    plt.subplot(221), plt.imshow(cv.cvtColor(resized, cv.COLOR_BGR2RGB))
    plt.title('Original Video Capture'), plt.axis('off')

    plt.subplot(222), plt.imshow(filtered_image_xy, cmap='gray')
    plt.title('SobelXY Edge Detector'), plt.axis('off')

    plt.subplot(223), plt.imshow(canny, cmap='gray')
    plt.title('Canny Edge Detector'), plt.axis('off')

    plt.subplot(224), plt.imshow(filtered, cmap='gray')
    plt.title('Laplacian Detector'), plt.axis('off')

    plt.draw()
    plt.pause(0.0001)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
