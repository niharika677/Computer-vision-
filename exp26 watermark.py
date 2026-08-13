import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Watermark text
text = "COMPUTER VISION"

# Position
position = (30, 50)

# Font
font = cv2.FONT_HERSHEY_SIMPLEX

# Add watermark
cv2.putText(
    img,
    text,
    position,
    font,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

# Save output
cv2.imwrite("watermarked_image.jpg", img)

# Display
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()