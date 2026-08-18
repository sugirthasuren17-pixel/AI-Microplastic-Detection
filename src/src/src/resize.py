import cv2

image = cv2.imread(
    "dataset/practice_images/beach1.jpg"
)

resized = cv2.resize(
    image,
    (224, 224)
)

cv2.imwrite(
    "dataset/processed_images/resized_beach1.jpg",
    resized
)

print("Image resized.")