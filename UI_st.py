import streamlit as st
from models import get_gemini_response, get_gemini_response_image, yt_summerize, imagegen
from PIL import Image
import io

## Initialize our Streamlit app
st.set_page_config(page_title="AIO GPT")

# Initialize session state for messages if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and "image_data" in message:
            image = Image.open(io.BytesIO(message["image_data"]))
            st.image(image, width=300)
        else:
            st.markdown(message["content"])

input_text = st.chat_input("Say something")

with st.sidebar:
    st.header("AIO Application")
    st.write("YouTube video summarization || Upload an image and ask about it || Ask to 'create image' of anything")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

response = ''
## If ask button is clicked
yt_url = "https://www.youtube.com"
keywords = ["create image", "generate image", "create picture", "generate picture"]
contains_keyword = any(keyword in (input_text or "").lower() for keyword in keywords)

if input_text:
    if contains_keyword:
        generated_image = imagegen(input_text)

        # Convert the image to a bytes buffer
        buffer = io.BytesIO()
        generated_image.save(buffer, format="PNG")
        image_data = buffer.getvalue()

        # Display the user input
        with st.chat_message("user"):
            st.markdown(input_text)

        # Display the generated image
        st.image(generated_image, width=300)

        # Append message and image data to session state
        st.session_state.messages.append({"role": "user", "content": input_text})
        st.session_state.messages.append({"role": "assistant", "image_data": image_data})
    elif yt_url in input_text:
        response = yt_summerize(input_text)
         with st.chat_message("user"):
            st.markdown(input_text)
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "user", "content": input_text})
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        if image:
            response = get_gemini_response_image(input_text, image)
        else:
            response = get_gemini_response(input_text)

        with st.chat_message("user"):
            st.markdown(input_text)
        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "user", "content": input_text})
        st.session_state.messages.append({"role": "assistant", "content": response})
