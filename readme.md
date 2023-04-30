# Paddington Resizer

This Python script allows you to automatically crop or add padding to images with a transparent background.

## Dependencies

This script requires the following Python libraries:

- Pillow (PIL)
- tqdm

You can install these libraries using pip: `pip install Pillow tqdm`

## Usage

1. Clone or download the repository.
2. Place your images in the 'source-images' folder.
3. Edit the variables in the paddington.py script as per your requirements:
    - `padding_ratio`: Set padding as a percentage, for example, 20 for 20%.
    - `image_ratio`: Optionally set image ratio in the format (width, height) or set it to None. Example: 9/16
4. Run the script: `python paddington.py`
5. The processed images will be available in the 'output-images' folder.