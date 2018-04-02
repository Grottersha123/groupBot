# -*- coding: utf-8 -*-


import requests
url = "https://api.telegram.org/bot502685712:AAFJL2QFZt0yKTNH-jJ9Hu_pCaoYLLG_u6Q/"



def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    # print(response.json())
    return response.json()


def last_update(data):
    # print(data)
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def postToTelegram(messages):



    # chat_id = get_chat_id(last_update(get_updates_json(url)))
    # print(chat_id)
    send_mess(-279392616,messages)
if __name__ == '__main__':
    # postToTelegram('lol')
    pass