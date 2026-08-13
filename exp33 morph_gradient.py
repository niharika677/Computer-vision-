import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Morphological gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Save output
cv2.imwrite("exp33 morph_gradient_output.jpg", gradient)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()