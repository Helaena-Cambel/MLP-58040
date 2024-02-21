import cv2 as cv
from matplotlib import pyplot as plt

img2 = cv.imread('dx.jpg')
img = cv.cvtColor(img2, cv.COLOR_RGB2BGR)
blur = cv.GaussianBlur(img, (10, 10), 0)



laplacian1 = cv.Laplacian(blur,1000,cv.CV_64F)
filtered1 = cv.convertScaleAbs(laplacian1)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(122), plt.imshow(filtered1, cmap='gray')
plt.title('Laplacian_Blur')
plt.axis('off')

plt.show()