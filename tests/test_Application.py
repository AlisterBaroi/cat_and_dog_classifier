# Testing functionalities in Application.py
from PIL import Image, ImageDraw
import numpy as np
import pytest, random, os
from Application import preprocess_image


# Create gradiant image for testing (wih random size and color range)
def create_test_image():
    w = random.randint(1, 1921)
    h = random.randint(1, 1081)
    image = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(image)
    # Define gradient colors
    color_start = (random.randint(0, 255), 0, 0)  # Random Start Color
    color_end = (0, 0, random.randint(0, 255))  # Random End Color
    # Create gradient
    for i in range(w):
        r = int(color_start[0] * (1 - i / w) + color_end[0] * (i / w))
        g = int(color_start[1] * (1 - i / w) + color_end[1] * (i / w))
        b = int(color_start[2] * (1 - i / w) + color_end[2] * (i / w))
        draw.line((i, 0, i, h), fill=(r, g, b))
    # image.save("test_image.png")
    return image


def test_preprocess_image_resize():
    print("\nChecking Image Size...")
    # Create a test image
    image = create_test_image()
    # Showing initial image size
    print("Image Size Before:", np.array(image).shape[0:2])
    # Image pre-processing here
    processed_image = preprocess_image(image)
    # Check if the processed image has the correct size (150 x 150)
    assert processed_image.shape[1:3] == (150, 150)
    print("Image Size After:", processed_image.shape[1:3])
    # os.remove("test_image.png")


def test_preprocess_image_normalize():
    print("\nChecking Image Color Range...")
    # Create a test image
    image = create_test_image()
    # Showing initial image color range
    print(
        "Image Range Before (Max, Min): ("
        + str(np.max(np.array(image)))
        + ", "
        + str(np.min(np.array(image)))
        + ")"
    )
    # Image pre-processing here
    processed_image = preprocess_image(image)
    # Check if the color values are normalized in the range [0, 1]
    assert np.max(processed_image) <= 1.0
    assert np.min(processed_image) >= 0.0
    print(
        "Image Range After (Max, Min): ("
        + str(np.max(processed_image))
        + ", "
        + str(np.min(processed_image))
        + ")"
    )
    # os.remove("test_image.png")
