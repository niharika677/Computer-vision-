import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Laplacian mask with positive center coefficient
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)

# Apply sharpening mask
sharpened = cv2.filter2D(img, -1, kernel)

# Save output
cv2.imwrite("laplacian_positive.jpg", sharpened)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()