import os
from PIL import Image

def compress_image(input_path, output_path, quality=85):
    
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Save the compressed image with a specific quality
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            print(f"Image compressed successfully. Saved at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def compress_folder_images(input_folder, output_folder, quality=85):
   
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Iterate through each file in the input folder
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Compose full paths for input and output images
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)

                # Compress the image
                compress_image(input_path, output_path, quality)

    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_folder_path = r'/media/prasad/2337-6F7E/MediaOptimizer/non_compress_folder'
output_folder_path = r'/media/prasad/2337-6F7E/MediaOptimizer/compressed_folder'
quality_level = 50

compress_folder_images(input_folder_path, output_folder_path, quality_level)
