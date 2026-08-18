import cv2

image = cv2.imread(
    "dataset/practice_images/beach1.jpg"
)

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

cv2.imwrite(
    "dataset/processed_images/gray_beach1.jpg",
    gray
)

print("Image converted.")