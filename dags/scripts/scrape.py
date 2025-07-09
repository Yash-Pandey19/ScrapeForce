import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = [tag.text for tag in soup.select(".titleline > a")]
    return titles
