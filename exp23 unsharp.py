import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Create blurred image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Create unsharp mask
mask = cv2.subtract(img, blur)

# Add mask to original image
sharpened = cv2.add(img, mask)

# Save output
cv2.imwrite("unsharp_output.jpg", sharpened)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Unsharp Masking", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()