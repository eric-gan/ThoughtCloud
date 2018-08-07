import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time

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

def scrape_livesite():
    driver = webdriver.Chrome()
    url = 'https://www.quora.com/topic/Astrophysics'
    driver.geturl(url)
    html = driver.page_source
    print(html)

scrape_livesite()
