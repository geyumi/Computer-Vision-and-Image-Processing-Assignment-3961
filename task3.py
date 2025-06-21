import cv2
import numpy as np
import os

os.makedirs('results', exist_ok=True)

def rotate_image(image_path, angle):
    img = cv2.imread(image_path)
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, rot_matrix, (w, h))
    filename = f'results/task3_rotate_{angle}deg.png'
    cv2.imwrite(filename, rotated)
    print(f'Saved: {filename}')


image_path = 'input_image.jpg'
for angle in [45, 90]:
    rotate_image(image_path, angle)
