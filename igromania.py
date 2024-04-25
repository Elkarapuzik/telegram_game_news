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

from config import *


def get_igromania_info(igromania_link_base, igromania_session):

    headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    while True:
        try:
            response1 = igromania_session.get(f"https://www.igromania.ru/igrovyie-novosti/", headers=headers)
            response1.raise_for_status()
            break
        except:
            cprint("Igromania site request error", 'red')
            time.sleep(DELAY)
            


    soup1 = BeautifulSoup(response1.text, features="html.parser")

    last_news_headline = soup1.find('a', attrs={"class": "ShelfCard_cardLink__mSxdR"}).text
    
    last_news_source_link = igromania_link_base + soup1.find('a', attrs={"class": "ShelfCard_cardLink__mSxdR"})['href']
    
    while True:
        try:
            responce2 = igromania_session.get(last_news_source_link)
            responce2.raise_for_status()
            break
        except:
            cprint("Igromania picure site request error", 'red')
            time.sleep(DELAY)


    soup2 = BeautifulSoup(responce2.text, features="html.parser")

    last_news_picture_url1 = soup2.find('figure', attrs={"class":"MaterialCommonImage_image__GyFHp material-common-image MaterialCommonImage_withCaption__wt5H2"})

    last_news_picture_url2 = last_news_picture_url1.find('img')['src']

    return last_news_headline, last_news_picture_url2, last_news_source_link 


def generate_post(headline,source_link):
    post = (f"""\
{headline} 
[▶▶▶Источник]({source_link})
""")
    return post


if __name__ == "__main__":

    igromania_session = requests.Session()

    igromania_link = 'https://www.igromania.ru'
    

    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    bot = telegram.Bot(token=telegram_bot_token)

    while True:
        igromania_headline, igromania_picture_url, igromania_source_link = get_igromania_info(igromania_link, igromania_session)

        igromania_post = generate_post(headline = igromania_headline , source_link = igromania_source_link)

        with open("igromania_last_headline.txt", "r", encoding="cp1251") as my_file:
            igromania_last_headline = my_file.read()

        if igromania_headline != igromania_last_headline:
            bot.send_photo(chat_id=telegram_chat_id, photo = igromania_picture_url , caption = igromania_post, parse_mode="Markdown")
            with open("igromania_last_headline.txt", "w", encoding="cp1251") as my_file:
                my_file.write(igromania_headline)
        
        time.sleep(DELAY)

