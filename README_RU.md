# Телеграм бот по игровым новостям
- Это программа которая автоматически присылает фотки и сообщения в телеграм используя базу данных coopland и igromania
<p align="center">
<img src="https://github.com/Elkarapuzik/telegram_game_news/blob/main/img/example.PNG" style="width:30%"/>
<img src="https://github.com/Elkarapuzik/telegram_game_news/blob/main/img/example228.PNG" style="width:30%"/>
</p>
## Как установить
- Скачайте репозиторий с гит хаба:

```
https://github.com/Elkarapuzik/telegram_game_news
```

- Python3 должен быть уже установлен. После используйте pip(или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
``` 
## Подготовка к запуску
- Создайте свой телеграмм канал
- Создайте бота и получите его токен
- Создайте в папке с программной файл `.env`
- Файл `.env` должен иметь следующий вид:
```
TELEGRAM_BOT_TOKEN=*API телеграм токен*
TELEGRAM_CHAT_ID=*Ссылка на канал с @ вместо t.me/*(пример : @stelegram_sigma)
```

## Как запустить программу
- Нужно открыть 2 терминала
- Чтобы запустить программу нужно ввести в 1 командную строку:
```
python3 coopland.py
```
- Чтобы запустить программу нужно ввести во 2 командную строку:
```
python3 igromania.py
```
