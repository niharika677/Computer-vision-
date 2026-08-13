import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Blur the image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# High-boost factor
A = 2.0

# High-boost filtering
high_boost = cv2.addWeighted(img, A, blur, -(A - 1), 0)

# Save output
cv2.imwrite("high_boost_output.jpg", high_boost)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("High Boost Image", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()