import os
import shutil
import datetime
import shortuuid

def copy_images(src_dir, dst_dir, num_images):
    """Copy a specified number of image files from a source directory to a destination directory.

    Args:
        src_dir (str): The path to the source directory containing the images.
        dst_dir (str): The path to the destination directory to copy the images to.
        num_images (int): The maximum number of images to copy.

    Returns:
        None
    """

    # Initialize counter
    counter = 0

    # Loop through all subdirectories in the source directory
    for root, dirs, files in os.walk(src_dir):
    
        # Loop through all files in each subdirectory
        for filename in files:
            # Check if the file is an image
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                id = str(shortuuid.ShortUUID().random(length=10))
                # Build the paths to the source and destination files
                src_path = os.path.join(root, filename)
                dst_path = os.path.join(dst_dir, f"{id}_" + filename)
                # Check if the maximum number of images has been reached
                if counter >= num_images:
                    return
                # Copy the file to the destination directory
                shutil.copyfile(src_path, dst_path)
                # Increment counter
                counter += 1


# copy_images("/Users/parvashah/Downloads/img", "static/img", num_images=10000)