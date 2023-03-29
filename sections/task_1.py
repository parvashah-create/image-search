import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from pathlib import Path
import streamlit as st


def task_1():
        
    # Read image features
    fe = FeatureExtractor()
    features = []
    img_paths = []
    for feature_path in Path("./static/feature").glob("*.npy"):
        features.append(np.load(feature_path))
        img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
    features = np.array(features)


    st.title("Image Retrieval")

    # Upload query image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Save query image
        img = Image.open(uploaded_file)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + uploaded_file.name
        img.save(uploaded_img_path)

        # Run search
        query = fe.extract(img)
        dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
        ids = np.argsort(dists)[:10]  # Top 10 results
        scores = [(dists[id], img_paths[id]) for id in ids]

        # Display top results
        st.image(uploaded_file, caption="Query Image", use_column_width="auto")
        for score in scores:
            st.image(str(score[1]), caption=f"Distance: {score[0]:.2f}", use_column_width="auto")



