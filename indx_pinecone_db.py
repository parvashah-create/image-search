import pinecone
import os
import requests
import shortuuid
import tqdm
import numpy as np
from PIL import Image
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



def process_images(img_dir, model):
    vectors = []

    preprocess = Compose([
        Resize(256),
        CenterCrop(224),
        ToTensor(),
        Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    for file_name in os.listdir(img_dir):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            img_path = os.path.join(img_dir, file_name)
            img = Image.open(img_path)
            embedding = model(preprocess(img).unsqueeze(0)).tolist()
            vector = {'id':str(file_name), 'values':embedding[0]}
            vectors.append(vector)

    return vectors




def new_index(index_name,dim):

    pinecone_api_key = config("PINECONE_API_KEY")
    pinecone.init(api_key=pinecone_api_key, environment="us-west4-gcp")

    model = torchvision.models.squeezenet1_1(pretrained=True).eval()

    # if the index does not already exist, we create it
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(name=index_name, dimension=dim)
    
    # instantiate connection to your Pinecone index
    index = pinecone.Index(index_name)
    vectors = process_images(img_dir="static/img",model=model)
    index.upsert(vectors)
    check  = index.describe_index_stats()

    return check

INDEX_NAME = 'pinecone-image-search'
INDEX_DIMENSION = 1000

print(new_index(INDEX_NAME,INDEX_DIMENSION))
