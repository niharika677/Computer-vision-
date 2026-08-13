import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Boundary detection kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply convolution
boundary = cv2.filter2D(gray, cv2.CV_32F, kernel)

# Convert to 8-bit
boundary = cv2.convertScaleAbs(boundary)

# Save output
cv2.imwrite("boundary_output.jpg", boundary)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Boundary Image", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()