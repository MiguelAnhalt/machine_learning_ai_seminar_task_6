# Task 6.2: Kitchenware Image Processing
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os  # Add os module for directory operations

# Loop to read and write automatic edge-detected images 
# Get all image files from the directory

kitchenware_list = ['cups', 'plates', 'dishes']

# Loop through each kitchenware type
for kitchenware in kitchenware_list:

    image_dir = f'machine_learning_ai_seminar_task_6/data/my_data/test/{kitchenware}'
    output_dir = f'machine_learning_ai_seminar_task_6/data/my_data/edge_detected/test/{kitchenware}'

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get all jpg/JPG files from the directory
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg'))]

    for image_file in image_files:
        # Construct full file paths
        input_path = os.path.join(image_dir, image_file)
        output_path = os.path.join(output_dir, image_file)

        # Read and process image
        img = cv2.imread(input_path, 0)
        if img is not None:
            print(f"Processing {image_file}, shape: {img.shape}")
            edges = cv2.Canny(img, 100, 200)
            cv2.imwrite(output_path, edges)
        else:
            print(f"Failed to read image: {image_file}")

    # Visualizing grayscaled and edged images
    img = cv2.imread(f'machine_learning_ai_seminar_task_6/data/my_data/test/{kitchenware}/1.1.jpg',0)
    edges = cv2.Canny(img,100,200)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

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