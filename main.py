from pprint import pprint

#______________________________

import requests
from termcolor import cprint
from bs4 import BeautifulSoup

#______________________________

def get_coopland_info():

    response = requests.get(f"https://coop-land.ru/helpguides/new/")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features="html.parser")

    last_news_headline = soup.find('h2').text

    last_news_description = soup.find('div', attrs={"class": "preview-text"}).text

    last_news_block = soup.find('div', attrs={"class": "article clr"})

    last_news_picture_url = 'https://coop-land.ru' + last_news_block.find('img')['data-src']
    
    last_news_source_link = last_news_block.find('a')['href']
    
    return last_news_headline, last_news_description, last_news_picture_url, last_news_source_link

coopland_headline, coopland_descriotipn, coopland_picture_url, coopland_source_link = get_coopland_info()

cprint(coopland_descriotipn, 'green')
cprint(coopland_headline, 'green')
cprint(coopland_source_link, 'yellow')
cprint(coopland_picture_url , 'yellow')
