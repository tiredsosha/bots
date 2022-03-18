import requests
import telebot

from bs4 import BeautifulSoup


def humor():
    humor = requests.get('https://baneks.ru/random', timeout=10)
    humor = humor.text
    try:
        soup = BeautifulSoup(humor, 'html.parser')
        text = soup.find("p").text
    except UnicodeDecodeError:
        text = 'Китайские дети утром делают зарядку, а вечером относят её в "Евросеть"'

    return text


def main():
    KEYS = [
        'шутк', 'анек', 'смех', 'юмор', 'смеш', 'смея', 'хохот', 'ржак', 'ржек'
    ]
    TOKEN = "2017247877:AAEV5Ut9X7L-waPumKRFquAKiaO43FJsEHk"
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(
            message,
            "привет, я саша шутко, добавь меня в чат и я буду сыпать лучшими шутками категории б\nкаждый раз когда в предложении будет упоминаться слово шутка или слова с корнем анек"
        )

    @bot.message_handler(func=lambda message: True)
    def text(message):
        msg = message.text.lower()
        for i in KEYS:
            if i in msg:
                bot.reply_to(message, humor())
                break

    bot.infinity_polling()


if __name__ == '__main__':
    main()