
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import time
import requests
from PIL import Image
import io
from internetData import main
import random

api_keys = ["AIzaSyBhfUMISwrJyU9LibvbcP-qK26j4HrdIEg","AIzaSyCywxL3BTdCMWt22qmZIxpOJVECFNbr02s"]

# Configure the Google Generative AI client
genai.configure(api_key=random.choice(api_keys))
model = genai.GenerativeModel('gemini-1.5-pro-latest')
model_video = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
chat = model.start_chat(history=[])

def yt_summerize(url):
    try:
        video_id = url.split("=")[1]
        trans_text = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        transcript = " ".join([i["text"] for i in trans_text])
        return get_gemini_response(transcript)
    except Exception as e:
        raise e

def get_gemini_response_image(input_text, image):
    response = model.generate_content([input_text, image])
    return response.text

def get_gemini_response(input_text):

    #realdata = main(input_text)
   
    #prompt = f"Below is some information retrieved from various internet sources related to your query:real time data:{realdata} Based on the above real-time information and your own knowledge, please provide a comprehensive response to the following query. If the query is about real-time or current data, prioritize using the provided real-time information along with your internal knowledge to generate a complete and detailed response:user question:{input_text}"
    response = chat.send_message(input_text)
    return response.text

def video_analysis(video_file_name):
    print(f"Uploading file...")
    video_file = genai.upload_file(path=video_file_name)
    print(f"Completed upload: {video_file.uri}")

    while video_file.state.name == "PROCESSING":
        print('.', end='')
        time.sleep(10)
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError(video_file.state.name)

    prompt = "Describe this video."
    print("Making LLM inference request...")
    response = model_video.generate_content([prompt, video_file], request_options={"timeout": 600})
    return response.text

def imagegen(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer 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"}

    payload = {
        "inputs": prompt,
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    image = Image.open(io.BytesIO(response.content))
    return image
