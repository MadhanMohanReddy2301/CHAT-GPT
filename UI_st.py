import streamlit as st
from models import get_gemini_response, get_gemini_response_image, yt_summerize, imagegen
from PIL import Image
import io



##initialize our streamlit app
st.set_page_config(page_title="AIO GPT")

input=st.text_area("Input Prompt: ",key="input")
submit=st.button("submit")

with st.sidebar:
    st.header("AIO Application")
    st.write("Youtube video summarization || Upload a image and ask about it || ask to -create image- of anything" )


    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        

response = ''
## If ask button is clicked
yt ="https://www.youtube.com"
list = ["create image", "generate image", "create picture", "generate picture"]
contains_keyword = any(keyword in input.lower() for keyword in list)

if submit:
    if  contains_keyword:
        st.write("Generating image...")
        image = imagegen(input)
        # Display the image in Streamlit
        st.image(image)
        
    elif yt in input:
        response = yt_summerize(input)
        st.subheader("Key Points from the video")
        st.write(response)
    else:    
        if image != "":
            response = get_gemini_response_image(input, image)
            
        else:
            
            response = get_gemini_response(input)
        st.subheader("Responses:")
        for chunk in response:
            st.write(chunk.text, end='')
        
