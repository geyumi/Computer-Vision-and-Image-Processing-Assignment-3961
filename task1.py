import cv2
import numpy as np
import os

os.makedirs('results', exist_ok=True)

def reduce_intensity_levels(image_path, levels):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    max_intensity = 255
    bins = 256 // levels
    reduced_img = (img // bins) * bins
    filename = f'results/task1_reduced_{levels}_levels.png'
    cv2.imwrite(filename, reduced_img)
    print(f'Saved: {filename}')

# Example usage
image_path = 'input_image.jpg'
for levels in [2, 4, 8, 16]:
    reduce_intensity_levels(image_path, levels)
