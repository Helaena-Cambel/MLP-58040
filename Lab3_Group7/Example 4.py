import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('noisy.jpg')

blur = cv.bilateralFilter(img, 10, 500, 50)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

