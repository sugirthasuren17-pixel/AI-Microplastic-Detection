import cv2

image = cv2.imread(
    "dataset/practice_images/beach img 1.jpeg"
)

print("Image loaded successfully!")

print("Image dimensions:", image.shape)