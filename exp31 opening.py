import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Opening = Erosion followed by Dilation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Save output
cv2.imwrite("opening.jpg", opening)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Opening", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()