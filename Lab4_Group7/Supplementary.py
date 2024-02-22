import cv2 as cv; import numpy as np
vid = cv.VideoCapture(0)
while (True):
    ret, frame = vid.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# SobelXY, Canny, and Laplacian Edge Detector
    sobelxy = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    sobelxy1 = cv.convertScaleAbs(sobelxy)
    canny = cv.Canny(gray, 100, 200)
    laplacian = cv.Laplacian(gray, cv.CV_64F)
    laplacian1 = cv.convertScaleAbs(laplacian)
# Resizing the edge detectors to combine all in one frame
    lapresize = cv.resize(laplacian1, (gray.shape[1], gray.shape[0]))
    sobresize = cv.resize(sobelxy1, (gray.shape[1], gray.shape[0]))
    canresize = cv.resize(canny, (gray.shape[1], gray.shape[0]))
    combine1 = np.hstack((gray, sobresize))
    combine2 = np.hstack((canresize, lapresize))
    final = np.vstack((combine1, combine2))
    FINAL_NA = cv.resize(final, (610, 400))
# Inserting labels
    cv.putText(FINAL_NA, 'GrayScale', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    cv.putText(FINAL_NA, 'SobelXY', (gray.shape[1] - 325, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    cv.putText(FINAL_NA, 'Canny', (10, gray.shape[0] - 245), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    cv.putText(FINAL_NA, 'Laplacian', (gray.shape[1] - 325, gray.shape[0] - 245), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    cv.imshow('Edge Detectors', FINAL_NA)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()

