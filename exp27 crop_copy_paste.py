import cv2

# Read source and destination images
source = cv2.imread("image.jpg")
destination = cv2.imread("image2.jpg")

if source is None:
    print("image.jpg not found")
    exit()

if destination is None:
    print("image2.jpg not found")
    exit()

# Crop region from source image
crop = source[50:200, 50:200]

# Get crop dimensions
h, w = crop.shape[:2]

# Paste position
x = 100
y = 100

# Check destination size
if y + h > destination.shape[0] or x + w > destination.shape[1]:
    print("Crop does not fit in destination image")
    exit()

# Paste crop into destination
destination[y:y+h, x:x+w] = crop

# Save output
cv2.imwrite("crop_copy_paste.jpg", destination)

# Display
cv2.imshow("Source Image", source)
cv2.imshow("Result", destination)

cv2.waitKey(0)
cv2.destroyAllWindows()