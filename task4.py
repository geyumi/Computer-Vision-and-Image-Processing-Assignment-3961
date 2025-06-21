import cv2
import numpy as np
import os

os.makedirs('results', exist_ok=True)

def block_average(image_path, block_size):
    img = cv2.imread(image_path)
    h, w, c = img.shape
    output = np.zeros_like(img)

    for y in range(0, h - h % block_size, block_size):
        for x in range(0, w - w % block_size, block_size):
            block = img[y:y+block_size, x:x+block_size]
            avg_color = block.mean(axis=(0, 1)).astype(np.uint8)
            output[y:y+block_size, x:x+block_size] = avg_color

    filename = f'results/task4_block_{block_size}x{block_size}.png'
    cv2.imwrite(filename, output)
    print(f'Saved: {filename}')


image_path = 'input_image.jpg'
for block_size in [3, 5, 7]:
    block_average(image_path, block_size)
