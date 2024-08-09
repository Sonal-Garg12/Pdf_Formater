from PIL import Image
import os

def resize_image(input_path, output_path, width, height, min_size_kb, max_size_kb, dpi):
    img = Image.open(input_path)
    img = img.resize((width, height), Image.LANCZOS)

    # Adjust quality to fit size constraints
    for quality in range(100, 0, -5):
        img.save(output_path, "JPEG", quality=quality, dpi=(dpi, dpi))
        if min_size_kb * 1024 <= os.path.getsize(output_path) <= max_size_kb * 1024:
            break

def convert_multiple_images(image_paths, output_dir, width, height, min_size_kb, max_size_kb, dpi):
    os.makedirs(output_dir, exist_ok=True)
    
    for image_path in image_paths:
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        resize_image(image_path, output_path, width, height, min_size_kb, max_size_kb, dpi)

# Example usage
image_paths = [
    
"ashi-photo.jpg","amaan-p.jpg","hooriya-photo.jpg","moiza-p.jpg","roshan-p.jpg","tayaba-photo.jpg","umar-photo.jpg" 
    
]
output_dir = "pdfoutput"
convert_multiple_images(image_paths, output_dir, 132, 170, 5, 20, 110)  # Set DPI to 110
