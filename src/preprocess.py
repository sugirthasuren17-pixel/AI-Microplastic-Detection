import cv2
from pathlib import Path

# Folder containing the original practice images
input_folder = Path("dataset/practice_images")

# Folder where processed images will be saved
output_folder = Path("dataset/processed_images")

# Create the output folder if it does not already exist
output_folder.mkdir(parents=True, exist_ok=True)

# Supported image formats
image_extensions = {".jpg", ".jpeg", ".png"}

# Process every image in the input folder
for image_path in input_folder.iterdir():

    # Skip files that are not images
    if image_path.suffix.lower() not in image_extensions:
        continue

    # Read the image
    image = cv2.imread(str(image_path))

    # Check whether OpenCV could read it
    if image is None:
        print(f"Could not read: {image_path.name}")
        continue

    # Resize the image to 224 x 224
    resized = cv2.resize(image, (224, 224))

    # Reduce small amounts of image noise
    denoised = cv2.GaussianBlur(resized, (5, 5), 0)

    # Create the output filename
    output_path = output_folder / f"{image_path.stem}_processed.jpg"

    # Save the processed image
    cv2.imwrite(str(output_path), denoised)

    print(f"Processed: {image_path.name}")

print("All images processed successfully!")