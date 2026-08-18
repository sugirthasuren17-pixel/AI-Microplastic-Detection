import cv2

image = cv2.imread("dataset/practice_images/beach1.jpg")

if image is None:
    print("Image could not be loaded.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    cv2.imwrite(
        "dataset/processed_images/beach1_edges.jpg",
        edges
    )

    print("Edge image created successfully!")