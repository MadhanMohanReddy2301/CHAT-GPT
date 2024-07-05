from googlesearch import search
import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=2):
    return search(query, num_results)

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract the title
    title = soup.title.string if soup.title else "No Title"
    # Extract all text within the body tag
    body = soup.body
    if body:
        body_text = body.get_text(separator='\n', strip=True)
    else:
        body_text = "No Body Content"
    return title, body_text

def main(query1):
    query = query1
    num_urls = 2
    urls = google_search(query, num_results=num_urls)
    collected_data = ""

    for i, url in enumerate(urls):
        print(f"Fetching URL {i + 1}: {url}")
        html_content = fetch_page_content(url)
        if html_content:
            title, body_text = extract_body_content(html_content)
            print(f"Title: {title}")
            print("Body Content:")
            print(body_text)
            print("\n" + "="*80 + "\n")
            collected_data += f"Title: {title}\n{body_text}\n\n"

    return collected_data

