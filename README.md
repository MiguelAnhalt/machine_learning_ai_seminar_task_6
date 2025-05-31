# Kitchenware Image Processing

This project processes kitchenware images using OpenCV to perform edge detection and various thresholding operations.

## Setup Instructions

1. Make sure you have Python 3.x installed on your system.

2. Create a virtual environment (recommended):
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
.
├── data/
│   └── my_data/
│       ├── test/
│       │   └── cups/          # Input images
│       └── edge_detected/
│           └── test/
│               └── cups/      # Processed edge-detected images
├── Task6_2_Kitcheware_Image_processing.py
├── requirements.txt
└── README.md
```

## Usage

1. Place your input images in the `data/my_data/test/cups/` directory.

2. Run the script:
   ```bash
   python Task6_2_Kitcheware_Image_processing.py
   ```

The script will:
- Process all JPG/JPEG images in the input directory
- Generate edge-detected versions of the images
- Save the processed images in the `data/my_data/edge_detected/test/cups/` directory
- Display visualizations of the original and processed images

## Features

- Automatic edge detection using Canny algorithm
- Various thresholding techniques (Binary, Otsu's, etc.)
- Image visualization with histograms
- Batch processing of multiple images

## Dependencies

- opencv-python >= 4.8.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0

## Notes

- The script supports both .jpg and .JPG file extensions
- Input images should be placed in the correct directory structure
- The output directory will be created automatically if it doesn't exist 