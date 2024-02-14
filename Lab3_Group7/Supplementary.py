import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('panda.jpg')
img2 = cv.imread('noisy.jpg')
blur1 = cv.blur(img1,(20,20))
blur2 = cv.GaussianBlur(img1,(5,5),0)
median = cv.medianBlur(img2, 11)
blur = cv.bilateralFilter(img2, 10, 500, 50)

plt.subplot(335),plt.imshow(img1)
plt.text(5, 5, 'Original', color='white', fontsize=10, ha='left', va='top')
plt.xticks([]), plt.yticks([])
plt.subplot(331),plt.imshow(blur1)
plt.text(5, 5, 'Blurred', color='white', fontsize=10, ha='left', va='top')
plt.xticks([]), plt.yticks([])
plt.subplot(333),plt.imshow(blur2)
plt.text(5, 5, 'Gaussian', color='white', fontsize=10, ha='left', va='top')
plt.xticks([]), plt.yticks([])
plt.subplot(337),plt.imshow(median)
plt.text(5, 5, 'Median', color='white', fontsize=10, ha='left', va='top')
plt.xticks([]), plt.yticks([])
plt.subplot(339),plt.imshow(blur)
plt.text(5, 5, 'Bilateral', color='white', fontsize=10, ha='left', va='top')
plt.xticks([]), plt.yticks([])

plt.show()











