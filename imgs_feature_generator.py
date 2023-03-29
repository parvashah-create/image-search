"""
This script extracts deep features from images using a pre-trained VGG16 model and saves the features as numpy arrays.

Usage:
    python extract_features.py

Output:
    - numpy arrays of deep features saved in the static/feature directory

Dependencies:
    - feature_extractor.py: defines the FeatureExtractor class for extracting deep features
    - PIL: Python Imaging Library for image processing
    - numpy: for saving deep features as numpy arrays
    - pathlib: for working with file paths

"""

from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np


if __name__ == '__main__':
    fe = FeatureExtractor()

    for img_path in sorted(Path("./static/img").glob("*.jpg")):
        print(img_path)  # e.g., ./static/img/xxx.jpg
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)
