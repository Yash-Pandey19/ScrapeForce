import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch page. Status: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    titles = [tag.text for tag in soup.select(".titleline > a")]
    return titles
