import cv2

image = cv2.imread("dataset/practice_images/beach1.jpg")

if image is None:
    print("Image could not be loaded.")
else:
    resized = cv2.resize(image, (224, 224))

    cv2.imwrite(
        "dataset/processed_images/beach1_resized.jpg",
        resized
    )

    print("Image resized successfully!")
    print("New dimensions:", resized.shape)