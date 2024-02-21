import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('dx.jpg')
img2 = cv.cvtColor(img1, cv.COLOR_RGB2BGR)
img_blur = cv.GaussianBlur(img1, (5, 5), 0)

sobelx = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
filtered_img_x = cv.convertScaleAbs(sobelx)
sobely = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
filtered_img_y = cv.convertScaleAbs(sobely)
sobelxy = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
filtered_img_xy = cv.convertScaleAbs(sobelxy)

plt.figure(figsize=(5, 5))
plt.subplot(221), plt.imshow(img2, cmap='gray'), plt.title('Original'), plt.axis("off")
plt.subplot(222), plt.imshow(filtered_img_x, cmap='gray'), plt.title('SobelX'), plt.axis("off")
plt.subplot(223), plt.imshow(filtered_img_y, cmap='gray'), plt.title('SobelY'), plt.axis("off")
plt.subplot(224), plt.imshow(filtered_img_xy, cmap='gray'), plt.title('SobelXY'), plt.axis("off")

plt.show()