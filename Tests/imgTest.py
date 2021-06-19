"""Tests Image File Path."""

import os

images_path = "../_data/photos/dog/"
imgs = os.listdir(images_path)
imgs = [images_path + item for item in imgs]
imgs = os.listdir(images_path)
print(imgs)
