from bs4 import BeautifulSoup
import requests

url = input('Write your url: \n')
tg = input('Tag: ')

html_page = requests.get(url).text

soup = BeautifulSoup(html_page, 'lxml')
tags = soup.find_all(tg, class_='listlink')
for t in tags:
    print(t.text)
    print('')

    