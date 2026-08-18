import cv2

image = cv2.imread("dataset/practice_images/beach1.jpg")

if image is None:
    print("Image could not be loaded.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(
        "dataset/processed_images/beach1_gray.jpg",
        gray
    )

    print("Grayscale image created successfully!")
    print("New dimensions:", gray.shape)