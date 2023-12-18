import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from openai import OpenAI
client = OpenAI()
init_api = os.environ.get("OPENAI_API_KEY")

import urllib.request
import shutil

st.set_page_config(page_title="Testing DALL E", page_icon=":robot:")
st.header("Testing DALL E")
st.markdown("---")
save_prompt = st.button('Save prompt?')
user_input = st.text_area("Enter some text here:")
submit = st.button('Generate')

def save_image_from_url(image_url, save_path):
    try:
        # Download the image from the URL
        with urllib.request.urlopen(image_url) as response, open(save_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        
        print(f"Image saved successfully to {save_path}")
    
    except Exception as e:
        print(f"Error: {e}")
        

def get_image(input):

    response = client.images.generate(
        model="dall-e-3",
        prompt=input,
        size="1024x1024",
        quality="standard",
        n=1
    )
    
    image_url = response.data[0].url

    st.image(image_url, width=200) # caption=input,
    #st.write(image_url)
    
    return image_url

current_datetime = datetime.now()


if submit:
    
    with st.spinner('Generating results...'):   
    
        image_url = get_image(user_input)
        
        formatted_datetime = current_datetime.strftime("%d_%m_%Y-_%H_%M_%S")
        save_image_from_url(image_url, "output/" + formatted_datetime + ".png")
        #st.success('Done!')



if save_prompt:
        with open('prompt_log.txt', 'a+') as file:        
            file.write("\n\n===============================\n\n")
            log_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
            file.write(log_time)
            file.write("\n")
            file.write(user_input)
    



     



