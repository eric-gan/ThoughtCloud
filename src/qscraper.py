import urllib.request
from bs4 import BeautifulSoup
url = 'https://conversationstartersworld.com/philosophical-questions/'
html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')
topics = []


def scrape_questions():
    data = []
    for line in soup.find_all('p'):
        new_entry = line.text
        if len(new_entry) != 0 and new_entry[len(new_entry) - 1] == '?':
            data.append(new_entry)
    return data
# for line in soup.find_all('h2'):
#     new_entry = line.text
#     print(new_entry)
#     if 'questions' in new_entry:
#         topics.append(new_entry)
