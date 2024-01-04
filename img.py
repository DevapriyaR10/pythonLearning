
import cv2   
from matplotlib import pyplot as plt

# Take image path as input
image_path = input("Enter the path of the image file: ")
img = cv2.imread(image_path)

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load the image.")
else:
    choice = int(input("""
    Enter your choice:
    1) Grey-Scale image processing
    2) Negative image processing\n"""))

    if choice == 1:
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Display the original and processed images using matplotlib
        plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image'), plt.axis('off')
        plt.subplot(1, 3, 2), plt.imshow(gray_img, cmap='gray'), plt.title('Grayscale'), plt.axis('off')
        plt.show()

    elif choice == 2:
        # Convert the image to negative
        neg_img = 255 - img
        plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image'), plt.axis('off')
        plt.subplot(1, 3, 2), plt.imshow(cv2.cvtColor(neg_img, cv2.COLOR_BGR2RGB)), plt.title('Negative Image'), plt.axis('off')
        plt.show()

    else:
        print("Invalid Choice!")
