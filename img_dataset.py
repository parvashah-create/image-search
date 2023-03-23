import os
import shutil
import glob
# Define the source and destination directories
src_dir = "/Users/parvashah/Downloads/img"
dst_dir = "/Users/parvashah/Documents/damg_7243/ass-4/static/img"


# Loop through all files in the source directory

# for gender in glob.glob(os.path.join("/Users/parvashah/Downloads/img", '*')):
#     for cloth_type in glob.glob(os.path.join(f"/Users/parvashah/Downloads/img/{gender}", '*')):
#         for listing in glob.glob(os.path.join(f"/Users/parvashah/Downloads/img/{gender}/{cloth_type}", '*')):
#             for filename in glob.glob(os.path.join(f"/Users/parvashah/Downloads/img/{gender}/{cloth_type}/{listing}", '*')):
#                 # Check if the file is an image
#                 if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
#                     # Build the paths to the source and destination files
#                     src_path = os.path.join(src_dir, filename)
#                     dst_path = os.path.join(dst_dir, filename)
#                     # Copy the file to the destination directory
#                     shutil.copyfile(src_path, dst_path)


import os
import shutil
import datetime

# Define the source and destination directories
src_dir = "/Users/parvashah/Downloads/img"
dst_dir = "/Users/parvashah/Documents/damg_7243/ass-4/static/img"
counter = 0

# Loop through all subdirectories in the source directory
for root, dirs, files in os.walk(src_dir):
    # Loop through all files in each subdirectory
    for filename in files:
        # Check if the file is an image
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            # Build the paths to the source and destination files
            src_path = os.path.join(root, filename)
            dst_path = os.path.join(dst_dir, f"{counter}_" + filename)
            # i want to get only 100 pictures
            if counter > 100:
                break
            counter += 1
                
            # Copy the file to the destination directory
            shutil.copyfile(src_path, dst_path)