import string
import requests
from bs4 import BeautifulSoup

def search_formatter(search):
    search_input = string.capwords(search)
    input_list = search_input.split()
    search_word = "_".join(input_list)

    if search_input == "Georgia":
        search_word += "_(U.S._state)"
    if search_input == "New York":
        search_word += " (state)"

    return search_word


def wiki_url(search_word):
    url = "https://en.wikipedia.org/wiki/"+search_word
    return url


def wikiscraper(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')

    labels = soup.find_all(class_='infobox-label')
    datas = soup.find_all(class_='infobox-data')

    results = dict()

    for x,y in zip(labels, datas):
        key = x.text
        value = y.text
        results[key] = value
        
    return results

# Used for "/search" route -- microservice for teammates
def formatted_wikiscraper(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')

    labels = soup.find_all(class_='infobox-label')
    datas = soup.find_all(class_='infobox-data')

    results = dict()

    for x,y in zip(labels, datas):
        key = x.text.encode('ascii', 'ignore').decode("utf-8")
        value = y.text.encode('ascii', 'ignore').decode("utf-8")
        results[key] = value
        
    return results


def flagscraper(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')

    image = soup.find("meta", property="og:image")
    image_url = image.get("content", None)
        
    return image_url
