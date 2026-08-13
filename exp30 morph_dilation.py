import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Save output
cv2.imwrite("morph_dilation.jpg", dilated)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Dilation", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()