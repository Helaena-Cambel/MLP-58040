import cv2 as cv

vid = cv.VideoCapture(0)
while (True):
    ret, frame = vid.read()

    #Sobel Edge Detector
    sobelxy = cv.Sobel(src=frame, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelxy)
    cv.imshow('Sobel Edge Detector', filtered_image_xy)

    #Canny Edge Detector
    canny = cv.Canny(frame, 100, 200)
    cv.imshow('Canny Edge Detector', canny)

    #Laplacian Edge Detector
    laplacian = cv.Laplacian(frame, 50, cv.CV_64F)
    filtered = cv.convertScaleAbs(laplacian)
    cv.imshow('Laplacian Detector', filtered)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()