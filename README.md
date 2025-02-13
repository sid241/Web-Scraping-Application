# Web-Scraping-Application

This Python script scrapes text from a webpage and summarizes it using OpenAI's GPT-3.  

## **Features**  
- Scrapes webpage text using **BeautifulSoup**.  
- Uses **OpenAI GPT-3** to generate a summary.  
- Allows users to specify the **webpage URL** and **summary length** via command-line arguments.  

## **Installation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **2. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3. Configure API Key**  
Create a `pass.yml` file in the project directory and add your **OpenAI API key**:  
```yaml
api: "your-openai-api-key"
```

## **Usage**  

Run the script with optional arguments:  
```sh
python scraper.py --web "https://example.com" --limit 100
```

- `--web`: (Optional) The URL of the webpage to scrape (default: GitHub repo).  
- `--limit`: (Optional) The maximum token limit for the summary (default: `100`).  

## **Example Output**  
```sh
Summary: This webpage discusses various Python applications for ChatGPT...
```

## **Requirements**  
- Python 3.x  
- `requests`  
- `beautifulsoup4`  
- `openai`  
- `pyyaml`  

## **License**  
This project is open-source under the MIT License.  

---
