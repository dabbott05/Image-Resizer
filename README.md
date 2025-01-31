# Image Resizer

## Features

### Resizes Images:
Resizes an image to new dimensions specified by the user.

### Supports Major Formats:
Leverages Pillow to handle most common image formats (JPEG, PNG, BMP, GIF, TIFF, etc.).

### Manual Resizing Implementation:
Uses a custom function that performs nearest-neighbor interpolation to map pixels from the original image to the resized image.

### User Input:
Accepts image path, desired width, and height through command-line input.

### Output Management:
Automatically creates an output directory (Resized Images) if it doesn't exist and saves the resized image there.

## Limitations / Stuff to add / Things to fix

### Nearest-Neighbor Interpolation Only:
The script uses a basic nearest-neighbor algorithm for resizing, which may lead to pixelation or blockiness when enlarging images. More advanced methods like bilinear or bicubic interpolation are not implemented.

### No Aspect Ratio Preservation:
The script does not automatically preserve the original image's aspect ratio. The user must manually input compatible dimensions.

### RGB Images Assumed:
The code creates the output image array with 3 channels (RGB). It may not handle images with an alpha channel (RGBA) correctly without modification.

### Minimal Error Handling:
Invalid file paths, unsupported formats, or incorrect inputs may cause runtime errors.

## How It Works

### Image Conversion:
The script converts the input image to a NumPy array to easily access and manipulate pixel data.

### Dimension Extraction:
It retrieves the original image's dimensions (height and width).

### New Image Creation:
A new NumPy array is initialized with the desired dimensions and a fixed channel size of 3 (for RGB).

### Scaling Calculation:
The script calculates horizontal (w_scale) and vertical (h_scale) scaling factors to map coordinates from the new image back to the original image.

### Pixel Mapping:
For each pixel in the new image, the corresponding pixel is taken from the original image using the calculated scaling factors (via nearest-neighbor interpolation).

### Output:
The new image array is converted back to a PIL Image object and saved in a designated output directory.

## Installation

### Clone the Repository
```
git clone https://github.com/yourusername/image-resizer.git
cd image-resizer
```

### Install Dependencies
This project requires Python 3 and the following packages:

#### NumPy
#### Pillow

### Install them via pip:
```
pip install numpy pillow
```
## Usage

### Run the script from the command line:
```
python image_resize.py
```
### When prompted, provide the following details:
```
Enter the image path: /path/to/myimage.jpg
Enter the new height: 300
Enter the new width: 400
```
### The script will generate an output file named myimage_resized.jpg in the Resized Images folder.


## Contributing

#### Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## License

#### Distributed under the MIT License. See LICENSE for more information.
