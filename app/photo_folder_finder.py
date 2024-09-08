"""Prints absolute paths to all folders that appear to be photograph folders."""

import os
from PIL import Image

def is_photograph(image_path):
    """Determines if an image meets the criteria to be considered a photograph."""
    try:
        with Image.open(image_path) as im:
            width, height = im.size
            return width > 100 and height > 100
    except OSError:
        return False

def main():
    """Walks through directories and prints paths of folders likely containing photographs."""
    for foldername, subfolders, filenames in os.walk('./'):
        photos = 0
        non_photos = 0

        for filename in filenames:
            if filename.lower().endswith(('jpg', 'png')):
                image_path = os.path.join(foldername, filename)
                if is_photograph(image_path):
                    photos += 1
                else:
                    non_photos += 1

        if photos > non_photos and photos > 0:
            print(os.path.abspath(foldername))

if __name__ == "__main__":
    main()
