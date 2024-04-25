# Telegram bot for gaming news
- This is a program that automatically sends pictures and messages to Telegram using the database coopland and igromania
<p align="center">
<img src="https://github.com/Elkarapuzik/telegram_game_news/blob/main/img/example.PNG" style="width:30%"/>
<img src="https://github.com/Elkarapuzik/telegram_game_news/blob/main/img/example228.PNG" style="width:30%"/>
</p>
## How to install
- Download the repository from the git hub:

```
https://github.com/Elkarapuzik/telegram_game_news
```

- Python3 should already be installed. Then use pip(or pip3 if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
``` 
## Prepare for launch
- Create your telegram channel
- Create a bot and get its token
- Create a `.env` file in the program folder.
- The `.env` file should have the following form:
```
TELEGRAM_BOT_TOKEN=*API telegram token*
TELEGRAM_CHAT_ID=*Link to channel with @ instead of t.me/*(example : @stelegram_sigma)
```

## How to run the program
- You need to open 2 terminals
- To run the program you need to enter in 1 command line:
```
python3 coopland.py
```
- To run the program you need to enter in the 2nd command line:
```
python3 igromania.py
```
