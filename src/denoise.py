import cv2

image = cv2.imread("dataset/practice_images/beach1.jpg")

if image is None:
    print("Image could not be loaded.")
else:
    denoised = cv2.GaussianBlur(image, (5, 5), 0)

    cv2.imwrite(
        "dataset/processed_images/beach1_denoised.jpg",
        denoised
    )

    print("Denoised image created successfully!")