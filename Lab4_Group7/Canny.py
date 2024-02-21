import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('dx.jpg.', 0)
edges = cv.Canny(img, 1, 2)

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('Canny')
plt.axis('off')

plt.show()