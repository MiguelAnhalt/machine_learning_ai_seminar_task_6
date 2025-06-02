"""
Title: Task Processing Kitchenware Images
Author: Subash Rajanayagam
Date: 04/2022
Description: 
# Necessary libraries via import
# URLS for OpenCV2: 
# Resoruce: https://www.andreasjakl.com/basics-of-ar-anchors-keypoints-feature-detection/pip-install-opencv-python/
# make sure you add python3 instead of python before your pip command if you have multiple
# python enviornments on your machine
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# Define the categories and paths
categories = ['cups', 'dishes', 'plates']
base_input_dir = 'data/my_data/test'
base_output_dir = 'data/my_data/edge_detected/test'

# Process images for each category
for category in categories:
    # Set up input and output paths for this category
    input_dir = os.path.join(base_input_dir, category)
    output_dir = os.path.join(base_output_dir, category)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all jpg/JPG files from the directory
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    print(f"\nProcessing {category} images...")
    
    # Process first image from each category for detailed comparison
    if image_files:
        # Read the first image
        img_path = os.path.join(input_dir, image_files[0])
        img = cv2.imread(img_path, 0)
        
        if img is not None:
            print(f"Creating detailed comparison for {category}/{image_files[0]}")
            # Apply edge detection
            edges = cv2.Canny(img, 100, 200)
            
            # Create comparison plot
            plt.figure(figsize=(10, 5))
            plt.subplot(121), plt.imshow(img, cmap='gray')
            plt.title('Original Image'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(edges, cmap='gray')
            plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
            plt.suptitle(f'Edge Detection - {category.capitalize()}', y=1.02, fontsize=16)
            plt.show()
            
            # Save edge-detected version
            output_path = os.path.join(output_dir, image_files[0])
            cv2.imwrite(output_path, edges)
    
    # Process remaining images with edge detection
    for image_file in image_files[1:]:
        input_path = os.path.join(input_dir, image_file)
        output_path = os.path.join(output_dir, image_file)
        
        img = cv2.imread(input_path, 0)
        if img is not None:
            print(f"Processing {category}/{image_file}, shape: {img.shape}")
            edges = cv2.Canny(img, 100, 200)
            cv2.imwrite(output_path, edges)
        else:
            print(f"Failed to read image: {category}/{image_file}")

print("\nProcessing complete! Check the generated plots for edge detection results.")

# Visualizing grayscaled and edged images
img = cv2.imread('data/my_data/test/cups/1.1.jpg',0)

# Applying various threshing of images
# Check the example at:
#  https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding
# More image processing can be found at: 
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()