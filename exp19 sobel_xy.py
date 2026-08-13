import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to 8-bit
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y
sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Save output
cv2.imwrite("sobel_xy.jpg", sobel_xy)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY", sobel_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()