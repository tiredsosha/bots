import requests
import vk_api

from bs4 import BeautifulSoup
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def send_some_msg(session, id, some_text):
    session.method("messages.send", {
        "chat_id": id,
        "message": some_text,
        "random_id": 0
    })


def humor():
    humor = requests.get('https://baneks.ru/random')
    humor = humor.text
    try:
        soup = BeautifulSoup(humor, 'html.parser')
        text = soup.find("p").text
    except UnicodeDecodeError:
        text = 'Китайские дети утром делают зарядку, а вечером относят её в "Евросеть"'

    return text


def main():
    vk_session = vk_api.VkApi(
        token=
        "a854d36c8ec3f8d48ca66afdf5825ca0a71bf208d224de629c8f574bc4aefa8697265b45568b208678e34"
    )
    longpool = VkBotLongPoll(vk_session, '207719465')

    for event in longpool.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.message.text.lower().split()
            id = event.chat_id
            if 'анекдотус' in msg:
                text = humor()
                send_some_msg(vk_session, id, text)


if __name__ == '__main__':
    main()