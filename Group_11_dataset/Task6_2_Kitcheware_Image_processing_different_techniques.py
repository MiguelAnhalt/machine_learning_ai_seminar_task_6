"""
Title: Kitchenware Image Edge Detection Comparison
Author: Subash Rajanayagam
Date: 04/2024
Description: 
This script compares different edge detection approaches for a single cup image:
1. Different image reading flags (grayscale, color, unchanged)
2. Different Canny edge detection thresholds
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def apply_edge_detection(img):
    """Apply Canny, Sobel, Laplacian edge detection, thresholding, and smoothing techniques to the input image."""
    results = {}
    
    # Apply Canny edge detection with different thresholds
    results['Canny (50,150)'] = cv2.Canny(img, 50, 150)    # Lower thresholds - more edges
    results['Canny (100,200)'] = cv2.Canny(img, 100, 200)  # Medium thresholds - balanced
    results['Canny (150,250)'] = cv2.Canny(img, 150, 250)  # Higher thresholds - fewer edges
    
    # Apply Sobel edge detection
    # Sobel in x direction
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    results['Sobel X'] = np.uint8(np.absolute(sobelx))
    
    # Sobel in y direction
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    results['Sobel Y'] = np.uint8(np.absolute(sobely))
    
    # Different weight combinations for Sobel
    # Equal weights (original)
    results['Sobel (0.5, 0.5)'] = cv2.addWeighted(
        results['Sobel X'], 0.5,
        results['Sobel Y'], 0.5, 0
    )
    
    # Emphasize horizontal edges
    results['Sobel (0.7, 0.3)'] = cv2.addWeighted(
        results['Sobel X'], 0.7,
        results['Sobel Y'], 0.3, 0
    )
    
    # Emphasize vertical edges
    results['Sobel (0.3, 0.7)'] = cv2.addWeighted(
        results['Sobel X'], 0.3,
        results['Sobel Y'], 0.7, 0
    )
    
    # Extreme weights
    results['Sobel (0.9, 0.1)'] = cv2.addWeighted(
        results['Sobel X'], 0.9,
        results['Sobel Y'], 0.1, 0
    )
    
    # Apply Laplacian edge detection with different kernel sizes
    # Convert to float32 for better precision
    img_float32 = np.float32(img)
    
    # Laplacian with kernel size 1 (default)
    results['Laplacian (ksize=1)'] = np.uint8(np.absolute(cv2.Laplacian(img_float32, cv2.CV_32F, ksize=1)))
    
    # Laplacian with kernel size 3
    results['Laplacian (ksize=3)'] = np.uint8(np.absolute(cv2.Laplacian(img_float32, cv2.CV_32F, ksize=3)))
    
    # Laplacian with kernel size 5
    results['Laplacian (ksize=5)'] = np.uint8(np.absolute(cv2.Laplacian(img_float32, cv2.CV_32F, ksize=5)))
    
    # Apply thresholding techniques
    # Basic Binary Thresholding
    _, results['Binary (90)'] = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)
    
    # Otsu's Thresholding
    _, results['Otsu'] = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Apply smoothing techniques
    # Gaussian Blur - only minimum and maximum
    results['Gaussian Blur (3x3)'] = cv2.GaussianBlur(img, (3, 3), 0)  # Minimum blur
    results['Gaussian Blur (21x21)'] = cv2.GaussianBlur(img, (21, 21), 0)  # Maximum blur
    
    # Median Blur - only minimum and maximum
    results['Median Blur (3)'] = cv2.medianBlur(img, 3)  # Minimum blur
    results['Median Blur (21)'] = cv2.medianBlur(img, 21)  # Maximum blur
    
    return results

def plot_comparison(original_img, processed_results, reading_flag):
    """Create five separate plots: Canny results, Sobel weight combinations, Laplacian results, thresholding results, and smoothing results."""
    # First plot: Canny results
    plt.figure(figsize=(15, 10))
    
    # Plot original grayscale image
    plt.subplot(2, 2, 1)
    if len(original_img.shape) == 3:  # Color image
        plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    else:  # Grayscale image
        plt.imshow(original_img, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.xticks([]), plt.yticks([])
    
    # Plot Canny edge detection results
    canny_techniques = ['Canny (50,150)', 'Canny (100,200)', 'Canny (150,250)']
    for idx, technique in enumerate(canny_techniques, 2):
        plt.subplot(2, 2, idx)
        plt.imshow(processed_results[technique], cmap='gray')
        plt.title(technique)
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.suptitle('Canny Edge Detection', y=1.02, fontsize=16)
    plt.show()
    
    # Second plot: Sobel results with different weights
    plt.figure(figsize=(15, 10))
    
    # Create a 2x3 grid for Sobel results
    # Plot original grayscale image
    plt.subplot(2, 3, 1)
    if len(original_img.shape) == 3:  # Convert to grayscale for Sobel
        plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY), cmap='gray')
    else:  # Already grayscale
        plt.imshow(original_img, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.xticks([]), plt.yticks([])
    
    # Plot different weight combinations
    weight_combinations = [
        ('Sobel (0.5, 0.5)', 'Equal Weights (0.5, 0.5)'),
        ('Sobel (0.7, 0.3)', 'Emphasize Horizontal (0.7, 0.3)'),
        ('Sobel (0.3, 0.7)', 'Emphasize Vertical (0.3, 0.7)'),
        ('Sobel (0.9, 0.1)', 'Strong Horizontal (0.9, 0.1)')
    ]
    
    # Plot weight combinations in remaining positions (2-6)
    for idx, (technique, title) in enumerate(weight_combinations, 2):
        plt.subplot(2, 3, idx)
        plt.imshow(processed_results[technique], cmap='gray')
        plt.title(title)
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.suptitle('Sobel Edge Detection with Different Weight Combinations', y=1.02, fontsize=16)
    plt.show()
    
    # Third plot: Laplacian results
    plt.figure(figsize=(15, 10))
    
    # Create a 2x2 grid for Laplacian results
    # Plot original grayscale image
    plt.subplot(2, 2, 1)
    if len(original_img.shape) == 3:  # Convert to grayscale
        plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY), cmap='gray')
    else:  # Already grayscale
        plt.imshow(original_img, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.xticks([]), plt.yticks([])
    
    # Plot Laplacian results with different kernel sizes
    laplacian_techniques = [
        'Laplacian (ksize=1)',
        'Laplacian (ksize=3)',
        'Laplacian (ksize=5)'
    ]
    
    for idx, technique in enumerate(laplacian_techniques, 2):
        plt.subplot(2, 2, idx)
        plt.imshow(processed_results[technique], cmap='gray')
        plt.title(technique)
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.suptitle('Laplacian Edge Detection with Different Kernel Sizes', y=1.02, fontsize=16)
    plt.show()
    
    # Fourth plot: Thresholding results
    plt.figure(figsize=(15, 5))
    
    # Create a 1x3 grid for thresholding results
    # Plot original grayscale image
    plt.subplot(1, 3, 1)
    if len(original_img.shape) == 3:  # Convert to grayscale
        plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY), cmap='gray')
    else:  # Already grayscale
        plt.imshow(original_img, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.xticks([]), plt.yticks([])
    
    # Plot thresholding results
    threshold_techniques = [
        ('Binary (90)', 'Binary Threshold (90)'),
        ('Otsu', "Otsu's Thresholding")
    ]
    
    for idx, (technique, title) in enumerate(threshold_techniques, 2):
        plt.subplot(1, 3, idx)
        plt.imshow(processed_results[technique], cmap='gray')
        plt.title(title)
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.suptitle('Thresholding Techniques Comparison', y=1.02, fontsize=16)
    plt.show()
    
    # Fifth plot: Smoothing results
    plt.figure(figsize=(15, 10))
    
    # Plot original grayscale image
    plt.subplot(2, 3, 1)
    if len(original_img.shape) == 3:  # Color image
        plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    else:  # Grayscale image
        plt.imshow(original_img, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.xticks([]), plt.yticks([])
    
    # Plot smoothing results
    smoothing_techniques = [
        # Gaussian Blur variations
        ('Gaussian Blur (3x3)', 'Gaussian Blur\nMinimum (3x3)'),
        ('Gaussian Blur (21x21)', 'Gaussian Blur\nMaximum (21x21)'),
        # Median Blur variations
        ('Median Blur (3)', 'Median Blur\nMinimum (3)'),
        ('Median Blur (21)', 'Median Blur\nMaximum (21)')
    ]
    
    for idx, (technique, title) in enumerate(smoothing_techniques, 2):
        plt.subplot(2, 3, idx)
        plt.imshow(processed_results[technique], cmap='gray')
        plt.title(title)
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.show()

def main():
    # Set up paths for cups category
    input_dir = os.path.join('data/my_data/test', 'cups')
    
    # Define reading flags to test
    reading_flags = {
        'Grayscale (0)': 0,      # Grayscale

    }
    
    # Get all jpg/JPG files from the directory
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    if image_files:
        # Read the first image with different flags
        img_path = os.path.join(input_dir, image_files[0])
        print(f"\nProcessing cup image: {image_files[0]}")
        
        for flag_name, flag_value in reading_flags.items():
            # Read image with current flag
            img = cv2.imread(img_path, flag_value)
            
            if img is not None:
                print(f"Processing with {flag_name}")
                
                # Convert color image to grayscale for edge detection if needed
                if len(img.shape) == 3:
                    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                else:
                    img_gray = img
                
                # Apply edge detection
                processed_results = apply_edge_detection(img_gray)
                
                # Create comparison plots
                plot_comparison(img, processed_results, flag_name)
            else:
                print(f"Failed to read image with {flag_name}")
    else:
        print("No images found in the cups directory")
    
    print("\nProcessing complete! Check the generated plots for edge detection comparisons.")

if __name__ == "__main__":
    main() 