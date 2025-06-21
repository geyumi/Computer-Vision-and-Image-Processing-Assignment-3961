import cv2
import os

os.makedirs('results', exist_ok=True)

def apply_average_blur(image_path, kernel_sizes):
    img = cv2.imread(image_path)
    for k in kernel_sizes:
        blurred = cv2.blur(img, (k, k))
        filename = f'results/task2_blur_{k}x{k}.png'
        cv2.imwrite(filename, blurred)
        print(f'Saved: {filename}')

# Example usage
image_path = 'input_image.jpg'
kernel_sizes = [3, 10, 20]
apply_average_blur(image_path, kernel_sizes)
