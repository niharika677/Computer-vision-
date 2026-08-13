import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(img, kernel, iterations=1)

# Save output
cv2.imwrite("morph_erosion.jpg", eroded)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Erosion", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()