from pprint import pprint
import time

#______________________________

import requests
from termcolor import cprint
from bs4 import BeautifulSoup
import telegram
import os
from dotenv import load_dotenv

load_dotenv()
#______________________________


def get_coopland_info(coopland_link_base):

    response = requests.get(f"https://coop-land.ru/helpguides/new/")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features="html.parser")

    last_news_headline = soup.find('h2').text

    last_news_description = soup.find('div', attrs={"class": "preview-text"}).text

    last_news_block = soup.find('div', attrs={"class": "article clr"})

    last_news_picture_url = coopland_link_base + last_news_block.find('img')['data-src']
    
    last_news_source_link = last_news_block.find('a')['href']
    
    return last_news_headline, last_news_description, last_news_picture_url, last_news_source_link

#________________________________________________________________________________________________________
if __name__ == "__main__":


    coopland_link = 'https://coop-land.ru'

    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    bot = telegram.Bot(token=telegram_bot_token)

    while True:
        coopland_headline, coopland_descriotipn, coopland_picture_url, coopland_source_link = get_coopland_info(coopland_link)

        post = (f"""\
{coopland_headline} 
{coopland_descriotipn}
[▶▶▶Источник]({coopland_source_link})
""")

#_______________________________________________________________

        bot.send_photo(chat_id=telegram_chat_id, photo = coopland_picture_url , caption = post, parse_mode="Markdown")
        time.sleep(300)




