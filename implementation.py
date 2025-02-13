import argparse
import requests
from bs4 import BeautifulSoup
import openai
import yaml

# Load API key from a YAML file
def load_api_key(file_path="pass.yml"):
    with open(file_path, "r") as f:
        credentials = yaml.safe_load(f)
    return credentials.get("api", None)

# Fetch webpage content from the given URL
def fetch_web_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the webpage. Status code: {response.status_code}")

# Extract all paragraph text from the HTML content
def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return " ".join([p.text for p in soup.find_all('p')])

# Trim text to fit within the OpenAI token limit
def truncate_text(text, max_chars=16132):
    return text[:max_chars] if len(text) > max_chars else text

# Generate a summary of the extracted text using OpenAI
def generate_summary(text, api_key, max_tokens=100):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text:\n{text}\n\nSummary:",
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Main function to handle argument parsing and execution
def main():
    parser = argparse.ArgumentParser(description="Web Scraping Summarizer")
    parser.add_argument('--web', type=str, default="https://github.com/xiaowuc2/ChatGPT-Python-Applications", help="Website URL to scrape")
    parser.add_argument('--limit', type=int, default=100, help="Maximum token limit for the summary")
    args = parser.parse_args()

    try:
        api_key = load_api_key()
        if not api_key:
            raise Exception("API key not found in pass.yml")
        
        html_content = fetch_web_content(args.web)
        raw_text = extract_text(html_content)
        trimmed_text = truncate_text(raw_text)
        summary = generate_summary(trimmed_text, api_key, args.limit)

        print(f"Summary: {summary}")
    except Exception as e:
        print(f"Error: {e}")

# Execute the script if run as the main program
if __name__ == "__main__":
    main()
