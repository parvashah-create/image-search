import numpy as np
from PIL import Image
from datetime import datetime
from pathlib import Path
import streamlit as st
import pinecone
from decouple import config
import torch
import torchvision
from torchvision.transforms import (
    Compose, 
    Resize, 
    CenterCrop, 
    ToTensor, 
    Normalize
)

def task_3():


    st.title("Image Retrieval")

    # Upload query image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"],key="task_3")
    preprocess = Compose([
    Resize(256),
    CenterCrop(224),
    ToTensor(),
    Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    if uploaded_file is not None:
        # Save query image
        img = Image.open(uploaded_file)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + uploaded_file.name
        img.save(uploaded_img_path)
        pinecone_api_key = config("PINECONE_API_KEY")
        pinecone.init(api_key=pinecone_api_key, environment="us-west4-gcp")

        model = torchvision.models.squeezenet1_1(pretrained=True).eval()
        
        # instantiate connection to your Pinecone index
        index = pinecone.Index("pinecone-image-search")

        query_vectors = model(preprocess(img).unsqueeze(0)).tolist()
        responses = index.query(vector=query_vectors, top_k=4)
        for res in responses["matches"]:
            images = Image.open(f'static/img/{res["id"]}')
            score = res["score"]
            st.image(images, caption=f"Distance: {score:.2f}", use_column_width="auto")



