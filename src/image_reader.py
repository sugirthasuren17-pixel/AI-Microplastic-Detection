import cv2

image = cv2.imread("dataset/practice_images/beach1.jpg")

if image is None:
    print("Image could not be loaded.")
else:
    print("Image loaded successfully!")
    print("Image dimensions:", image.shape)

    cv2.imshow("Practice Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()