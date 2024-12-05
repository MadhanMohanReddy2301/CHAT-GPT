# AIO GPT

AIO GPT is a powerful AI application that integrates multiple functionalities, including YouTube video summarization, image generation, and interactive conversations using Google's Generative AI (Gemini) model. It allows users to interact with AI through a chat interface, generate images based on user prompts, summarize YouTube videos, and analyze uploaded images.

## Features

- **YouTube Video Summarization:** Automatically summarize YouTube videos based on their transcript.
- **Image Generation:** Create images based on user input using Stable Diffusion model via Hugging Face API.
- **Interactive Chat:** Use the Google Generative AI (Gemini) model to generate intelligent responses for general queries.
- **Image Analysis:** Upload an image and ask the AI to provide a detailed response or description.

## Project Components

- **Google Generative AI (Gemini-1.5):** Used for generating responses to user queries and analyzing uploaded content.
- **YouTube Transcript API:** Fetches transcripts of YouTube videos for summarization.
- **Stable Diffusion (Hugging Face API):** Generates images based on user input.
- **Streamlit UI:** Provides an interactive user interface for the app.
- **Python Libraries:** Includes `requests`, `PIL`, `youtube_transcript_api`, and others to handle image and video processing.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MadhanMohanReddy2301/CHAT-GPT.git
    cd CHAT-GPT
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables for API keys:**

   Make sure to set up the necessary API keys for Google's Generative AI and the Hugging Face API by adding them to your environment or as variables in the project.

4. **Run the Streamlit app:**

    ```bash
    streamlit run UI_st.py
    ```

## Usage

- **YouTube Summarization:**  
  Paste the URL of a YouTube video, and the app will fetch the transcript and generate a summary.

- **Image Generation:**  
  Enter prompts like "create image of a sunset" or "generate picture of a cat," and the app will generate an image based on the description.

- **Interactive Chat:**  
  Ask general questions, and the app will respond using the Gemini model. The app supports text-based queries and can also provide image analysis for uploaded pictures.

## Example

- **YouTube Video Summarization:**
    - Input: "https://www.youtube.com/watch?v=VIDEO_ID"
    - Output: A summarized version of the video transcript.

- **Image Generation:**
    - Input: "Create image of a city at night"
    - Output: A generated image based on the prompt.

- **Interactive Chat:**
    - Input: "What is the capital of France?"
    - Output: "The capital of France is Paris."

## Files Structure

- **`UI_st.py`** - Main Streamlit app for the user interface.
- **`internetData.py`** - Handles data processing for real-time information retrieval (if enabled).
- **`models.py`** - Contains functions for interacting with Google's Gemini API, YouTube Transcript API, and image generation.
- **`requirements.txt`** - Lists the required Python packages for the project.

## Requirements

- Python 3.8+
- `requests`
- `PIL` (Pillow)
- `streamlit`
- `youtube_transcript_api`
- Google API credentials (for Gemini and YouTube API access)
- Hugging Face API key (for Stable Diffusion)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Madhan Mohan Reddy](https://github.com/MadhanMohanReddy2301)
