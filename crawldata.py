import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def download_image(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        filename = os.path.join(folder, os.path.basename(urllib.parse.urlparse(url).path))
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

def extract_background_image(style):
    # Extract the URL from the background-image style
    if 'background-image' in style:
        start = style.find('url(') + 4
        end = style.find(')', start)
        url = style[start:end].strip('"\'')
        return url
    return None

def crawl_images(page_url, folder='images'):
    try:
        os.makedirs(folder, exist_ok=True)
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all img tags and download their images
        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if img_url:
                img_url = urllib.parse.urljoin(page_url, img_url)
                download_image(img_url, folder)
        
        # Find all div tags with style attributes and extract background images
        divs = soup.find_all('div', style=True)
        for div in divs:
            style = div.get('style')
            img_url = extract_background_image(style)
            if img_url:
                img_url = urllib.parse.urljoin(page_url, img_url)
                download_image(img_url, folder)

    except requests.RequestException as e:
        print(f"Failed to retrieve the page: {e}")

# Example usage
page_url = 'path_here'
crawl_images(page_url)
