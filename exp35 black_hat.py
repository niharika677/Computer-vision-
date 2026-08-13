import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Create kernel
kernel = np.ones((9, 9), np.uint8)

# Black Hat transformation
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Save output
cv2.imwrite("exp35 black_hat_output.jpg", black_hat)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Black Hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()