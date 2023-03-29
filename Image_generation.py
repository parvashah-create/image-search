import os
import streamlit as st
import openai

openai.api_key = "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"



def generate_image(image_type):
    
    response = openai.Image.create(
    prompt= image_type,
    n=1,
    size="1024x1024"
    )
    image1 = response['data'][0]['url']
    st.image(image=image1, caption="Your customized fashion T-Shirt")

        
tshirt_type = st.text_input("Enter the T-Shirt type:", "")
image_type = tshirt_type

if image_type!="":
    generate_image(image_type)