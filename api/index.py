from fastapi import FastAPI
import requests
import fitz

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

def download_from_url(url):
    """
    Download content from a URL
    
    Args:
        url (str): URL to download content from
        
    Returns:
        bytes: Downloaded content
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.content
    except Exception as e:
        print(f"Error downloading from {url}: {str(e)}")
        raise Exception(f"Failed to download content from URL: {str(e)}")

@app.post("/api/py/extractPdfText")
def extract_pdf_text(file_content):
    """
    Extract text from PDF content
    
    Args:
        file_content (bytes or str): Either PDF file content as bytes or URL to PDF
        
    Returns:
        str: Extracted text from the PDF
    """
    # If file_content is a URL, download the content
    if isinstance(file_content, str) and (file_content.startswith('http://') or file_content.startswith('https://')):
        file_content = download_from_url(file_content)
    
    doc = fitz.open(stream=file_content, filetype="pdf")  # Open the PDF file
    text = ""
    for page in doc:  # Iterate through each page
        text += page.get_text()  # Extract text from the page
    return text.lower().replace("\n", " ").replace("  ", " ")  # Clean up the text