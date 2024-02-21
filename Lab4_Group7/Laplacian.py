#Laplacian Edge Detector
import cv2 as cv
from matplotlib import pyplot as plt

img2 = cv.imread('dx.jpg')
img = cv.cvtColor(img2, cv.COLOR_RGB2BGR)

laplacian = cv.Laplacian(img,5,cv.CV_64F)
filtered = cv.convertScaleAbs(laplacian)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(122), plt.imshow(filtered, cmap='gray')
plt.title('Laplacian')
plt.axis('off')

plt.show()