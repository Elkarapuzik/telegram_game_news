from pprint import pprint
import time
import os
#______________________________

import requests
from termcolor import cprint
from bs4 import BeautifulSoup
import telegram
from dotenv import load_dotenv

load_dotenv()

from config import *
#______________________________



def get_coopland_info(coopland_link_base, coopland_session):

    headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    while True:
        try:
            response = coopland_session.get(f"https://coop-land.ru/", headers=headers)
            response.raise_for_status()
            break
        except:
            cprint("coopland site request error", 'red')
            time.sleep(DELAY)

    soup = BeautifulSoup(response.text, features="html.parser")

    last_news_headline = soup.find('h2').text

    last_news_description = soup.find('div', attrs={"class": "preview-text"}).text

    last_news_block = soup.find('div', attrs={"class": "article clr"})

    last_news_picture_url = coopland_link_base + last_news_block.find('img')['data-src']
    
    last_news_source_link = last_news_block.find('a')['href']
    
    return last_news_headline, last_news_description, last_news_picture_url, last_news_source_link

def generate_post(headline,descriotipn,source_link):
    post = (f"""\
{headline} 
{descriotipn}
[▶▶▶Источник]({source_link})
""")
    return post


#________________________________________________________________________________________________________
if __name__ == "__main__":

    coopland_session = requests.Session()

    coopland_link = 'https://coop-land.ru'

    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    bot = telegram.Bot(token=telegram_bot_token)

    while True:
        coopland_headline, coopland_descriotipn, coopland_picture_url, coopland_source_link = get_coopland_info(coopland_link, coopland_session)

        coopland_post = generate_post(headline = coopland_headline , descriotipn = coopland_descriotipn , source_link = coopland_source_link)

        with open("coopland_last_headline.txt", "r", encoding="cp1251") as my_file:
            coopland_last_headline = my_file.read()

        if coopland_headline != coopland_last_headline:
            bot.send_photo(chat_id=telegram_chat_id, photo = coopland_picture_url , caption = coopland_post, parse_mode="Markdown")
            with open("coopland_last_headline.txt", "w", encoding="cp1251") as my_file:
                my_file.write(coopland_headline)

        time.sleep(DELAY)
#_______________________________________________________________