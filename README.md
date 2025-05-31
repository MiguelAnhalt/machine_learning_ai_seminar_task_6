# Kitchenware Image Processing

This project processes kitchenware images using OpenCV to perform edge detection and various thresholding operations. It provides tools for:
- Automatic edge detection using Canny algorithm
- Various thresholding techniques (Binary, Otsu's, etc.)
- Image visualization with histograms
- Batch processing of multiple images

## Project Setup

### 1. Environment Setup

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

### 2. Repository Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd kitchenware-image-processing
   ```

2. Configure Git (if not already done):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
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

## Dependencies

- opencv-python >= 4.8.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0

## Development Workflow

### Branch Management

#### Main Branches
- `main`: Production-ready code
- `develop`: Development branch for integration

#### Working with Branches

1. Create and switch to a new feature branch:
   ```bash
   # Create and switch to a new branch
   git checkout -b feature/your-feature-name
   
   # Example: For edge detection improvements
   git checkout -b feature/edge-detection
   ```

2. Create and switch to a bugfix branch:
   ```bash
   git checkout -b bugfix/issue-description
   
   # Example: For fixing image loading issues
   git checkout -b bugfix/image-loading
   ```

3. Working on your branch:
   ```bash
   # Make your changes
   git add .
   git commit -m "Descriptive message about your changes"
   
   # Push your branch to remote
   git push origin feature/your-feature-name
   ```

4. Merging your changes:
   ```bash
   # Switch to develop branch
   git checkout develop
   
   # Update develop branch
   git pull origin develop
   
   # Merge your feature branch
   git merge feature/your-feature-name
   
   # Push changes to remote
   git push origin develop
   ```

### Branch Naming Convention
- Feature branches: `feature/feature-name`
- Bug fixes: `bugfix/issue-description`
- Documentation: `docs/documentation-name`
- Hotfixes: `hotfix/issue-description`

### Git Workflow Best Practices

1. Always pull the latest changes before starting new work:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. Keep your branches up to date:
   ```bash
   git checkout feature/your-feature-name
   git rebase develop
   ```

3. Resolve conflicts if they occur:
   ```bash
   # During rebase or merge
   git status  # Check conflicting files
   # Resolve conflicts in your editor
   git add .   # Add resolved files
   git rebase --continue  # or git merge --continue
   ```

4. Clean up branches after merging:
   ```bash
   # Delete local branch
   git branch -d feature/your-feature-name
   
   # Delete remote branch
   git push origin --delete feature/your-feature-name
   ```

## Contributing

1. Always create a new branch for your work
2. Follow the branch naming convention
3. Write clear commit messages
4. Test your changes before pushing
5. Create a pull request to merge your changes into the develop branch

## Notes

- The script supports both .jpg and .JPG file extensions
- Input images should be placed in the correct directory structure
- The output directory will be created automatically if it doesn't exist
- Make sure to activate your virtual environment before running the script
- Keep your virtual environment's dependencies up to date using `pip install -r requirements.txt` 