import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('dx.jpg', 0)
edges = cv.Canny(img,1,2)

# show the first image
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis("off")

# show the second image
plt.subplot(222)
plt.imshow(edges, cmap='gray')
plt.title('Canny')
plt.axis("off")

# show the frame
plt.show()
