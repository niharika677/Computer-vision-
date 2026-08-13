import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate gradients
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert gradients to 8-bit
gx = cv2.convertScaleAbs(gx)
gy = cv2.convertScaleAbs(gy)

# Combine gradients
gradient = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

# Sharpen using gradient mask
sharpened = cv2.add(gray, gradient)

# Save output
cv2.imwrite("gradient_mask_output.jpg", sharpened)

# Display
cv2.imshow("Original Image", gray)
cv2.imshow("Gradient Masking", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()