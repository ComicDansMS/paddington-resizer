import os
from PIL import Image, ImageOps
from tqdm import tqdm

# Editable variables
source_folder = "source-images"
output_folder = "output-images"
padding_ratio = 100  # Set padding as percentage, set 0 for hardcrop
image_ratio = None  # Optionally set image ratio: (width, height) or None

def calculate_padding(img_size, padding_ratio):
    return int(img_size * (padding_ratio / 100))

def expand_canvas_to_ratio(img, ratio):
    img_width, img_height = img.size
    target_width = max(img_width, int(img_height * ratio[0] / ratio[1]))
    target_height = max(img_height, int(img_width * ratio[1] / ratio[0]))

    new_img = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
    new_img.paste(img, ((target_width - img_width) // 2, (target_height - img_height) // 2))
    return new_img

def add_padding(img, padding):
    border = (padding, padding, padding, padding)
    return ImageOps.expand(img, border, fill=(0, 0, 0, 0))

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_files = [
    f for f in os.listdir(source_folder) if f.lower().endswith((".png", ".webp"))
]

for file in tqdm(image_files, desc="Padding & resizing images", unit="image"):
    image_path = os.path.join(source_folder, file)
    img = Image.open(image_path).convert("RGBA")
    
    # Hardcrop: remove transparency around the image
    img = img.crop(img.getbbox())

    # Expand canvas to the required ratio (if provided)
    if image_ratio is not None:
        img = expand_canvas_to_ratio(img, image_ratio)

    # Apply padding
    if padding_ratio > 0:
        padding = calculate_padding(img.size[0], padding_ratio)
        img = add_padding(img, padding)
    
    # Save resized image
    output_path = os.path.join(output_folder, file)
    img.save(output_path, quality=90)