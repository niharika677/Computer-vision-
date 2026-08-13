import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Create kernel
kernel = np.ones((9, 9), np.uint8)

# Top Hat transformation
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Save output
cv2.imwrite("exp34 top_hat_output.jpg", top_hat)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()