import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os


def scrape_questions():
    url = 'https://conversationstartersworld.com/philosophical-questions/'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    for line in soup.find_all('p'):
        new_entry = line.text
        if len(new_entry) != 0 and new_entry[len(new_entry) - 1] == '?':
            data.append(new_entry)
    return data


def scrape_quora(topic=None):
    """
    Scrapes quora for questions on a given topic

    param topic: The topic to sort by
    type topic: str
    """
    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
    if topic is None:
        url = 'https://www.quora.com/topic/Science'
    else:
        url = 'https://www.quora.com/search?q=' + topic
    driver.get(url)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    for line in soup.find_all('span', class_="ui_qtext_rendered_qtext"):
        data.append(line.text)
    return data
