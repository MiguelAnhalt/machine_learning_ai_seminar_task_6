# Task 6.3: Load image and process
import tensorflow as tf             
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def set_data_path():
    # Desired image resolution
    img_height = 128
    img_width = 128

    # Location of train and test images
    dir_path = os.path.dirname(os.path.abspath(__file__))

    train_path = os.path.join(dir_path, 'data', 'my_data','test')
    test_path = os.path.join(dir_path, 'data', 'my_data', 'edge_detected', 'test')

    # Check if the directories exist
    if not os.path.exists(train_path):
        print(f"Training data path does not exist: {train_path}")
        sys.exit(1)
    
    print(f"Training data path: {train_path}")

    return train_path, test_path, img_height, img_width

# Prepare training data from image to tf.data.Dataset
# Check the tutorial: https://www.tensorflow.org/tutorials/load_data/images
# For seed,guarantee the same set of randomness [e.g. initializing weights of ANN, if not set, very different results can arrise]
def prepare_datasets(data_path_train, data_path_test, img_height, img_width):
    # Prepare training data from image to tf.data.Dataset
    ds_train = tf.keras.preprocessing.image_dataset_from_directory(
        data_path_train,
        color_mode='rgb',
        image_size=(img_height, img_width),  # reshape
        shuffle=False,
        seed=123,
    )

    # Prepare test data from image to tf.data.Dataset
    ds_validation = tf.keras.preprocessing.image_dataset_from_directory(
        data_path_test,
        color_mode='rgb',
        image_size=(img_height, img_width),  # reshape
        shuffle=False,
        seed=123,
    )
    
    return ds_train, ds_validation

def plot_sample_images(ds_train, ds_validation):
    # Retriving class names from the tf.data.Dataset of training data
    if hasattr(ds_train, 'class_names'):
        class_names = ds_train.class_names
        print(class_names)
    else:
        raise AttributeError("ds_train does not have attribute 'class_names'. Make sure ds_train is not converted to a list before this line.")

    # Retriving and displaying training images from tf.data.Dataset of training data
    plt.figure(figsize=(10, 10))
    for images, labels in ds_train:
        for i in range(min(18, images.shape[0])):
            ax = plt.subplot(5, 4, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")
    plt.tight_layout()
    plt.show() 

    # Retriving class names from the tf.data.Dataset of validation data
    if hasattr(ds_train, 'class_names'):
        class_names = ds_validation.class_names
        print(class_names)
    else:
        raise AttributeError("ds_train does not have attribute 'class_names'. Make sure ds_train is not converted to a list before this line.")
    
    # Retriving and displaying training images from tf.data.Dataset of validation data
    plt.figure(figsize=(10, 10))
    for images, labels in ds_validation:
        for i in range(min(9, images.shape[0])):
            ax = plt.subplot(5, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")
    plt.tight_layout()
    plt.show()  


if __name__ == "__main__":
    # Set data paths and image dimensions
    train_path, test_path, img_height, img_width = set_data_path()

    # Prepare datasets
    ds_train, ds_validation = prepare_datasets(train_path, test_path, img_height, img_width)

    # Plot sample images from training and validation datasets
    plot_sample_images(ds_train, ds_validation)