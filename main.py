from pprint import pprint

#______________________________

import requests
from termcolor import cprint
from bs4 import BeautifulSoup

#______________________________

main_url = 'https://coop-land.ru'
#Url for pictures


response = requests.get(f"https://coop-land.ru/helpguides/new/")
response.raise_for_status()

soup = BeautifulSoup(response.text, features="html.parser")

last_news_headline = soup.find('h2').text
cprint(last_news_headline, 'green')

last_news_description = soup.find('div', attrs={"class": "preview-text"}).text
cprint(last_news_description, 'green')

last_news_block = soup.find('div', attrs={"class": "article clr"})

last_news_picture_url = last_news_block.find('img')['data-src']
cprint(main_url + last_news_picture_url , 'red')

last_news_source_link = last_news_block.find('a')['href']
cprint(last_news_source_link, 'red')
