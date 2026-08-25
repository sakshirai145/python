import cv2
import matplotlib.pyplot as plt
from skimage.util import random_noise

# Read Image
image_path = "/Users/sakshismac/Downloads/Zenitsu.jpg"

img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
else:
    print("Image loaded successfully!")
    print("Image Shape:", img.shape)

    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display Original Image
    plt.figure(figsize=(8, 6))
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    # Resize Image
    resized = cv2.resize(img, (300, 300))

    plt.figure(figsize=(5, 5))
    plt.imshow(resized)
    plt.title("Resized Image")
    plt.axis("off")
    plt.show()

    # Add Gaussian Noise
    noisy = random_noise(img)

    plt.figure(figsize=(8, 6))
    plt.imshow(noisy)
    plt.title("Noisy Image")
    plt.axis("off")
    plt.show()