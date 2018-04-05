
import vk
import time as t
from telegramSendBot import *
from datetime import datetime

def send_message(api, user_id, message, **kwargs):
    data_dict = {
        'response': 5748248,
        'user_id': user_id,
        'message': message,
    }
    data_dict.update(**kwargs)
    return api.messages.send(**data_dict)


def openConfig(path):
    import configparser
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_api(access_token):
    session = vk.Session(access_token=access_token)
    return vk.API(session)



#Находит максимальное фото
def maxPhoto(lst):
    max = 0
    for photo in lst:
        if photo.find('photo_') != -1:
            ph = int(photo[6:])
            # print(ph)
            if ph > max:
                max = ph
    return 'photo_{}'.format(max)


# Берет всю информацию которая нужна для бота в телеграме. передается по одной записи
def takeInformathion(keys):
    lst = []
    flag = [False, False, False]
    if 'text' in keys:
        lst.append(keys['text'])
        if 'attachments' in keys:
            for tp in keys['attachments']:
                # tp = elem['attachments']
                if tp['type'] == 'link':
                    lst.append(tp['link']['title'])
                    lst.append(tp['link']['url'])
                elif tp['type'] == 'doc':
                    lst.append(tp['doc']['title'])
                    lst.append(tp['doc']['url'])
                elif tp['type'] == 'photo':
                    lst.append(tp['photo'][maxPhoto(list(tp['photo'].keys()))])
    return lst

                    # elif:
                    #     pass
def send_message(api, user_id, message, **kwargs):
    data_dict = {
        'user_id': user_id,
        'message': message,
    }
    data_dict.update(**kwargs)
    return api.messages.send(**data_dict)

def wallVkSend(wall,date):
    lst = []
    temp = wall[0]['date']
    print(temp)
    for post in wall:
        # print(post)
        if int(post['date']) != int(date):
            # print(post)
            primaryPost = takeInformathion(post)
            lst.append(primaryPost)
        else:
            break
    return lst,temp


def wallVkSendCurrentDate(wall,date):
    lst = []
    temp = wall[0]['date']
    print(temp)
    month = date.strftime('%d-%m-%Y')
    hour = int(date.strftime('%H%M%S'))
    for post in wall:
        # print(post)
        dt = datetime.fromtimestamp(post['date'])
        month1 = dt.strftime('%d-%m-%Y')
        hour1 = int(date.strftime('%H%M%S'))
        if month1 == month:
                    # print(post)
                    primaryPost = takeInformathion(post)
                    lst.append(primaryPost)

        else:
            break
    return lst,temp



if __name__ == '__main__':
    print(vk.__version__)
    # vk.logger.setLevel('DEBUG')
    session = vk.AuthSession(5748248, 'nastya_grotter@mail.ru', r'Grotter123', scope='wall, messages,offline')
    print(session.access_token)
    # print(session)
    # vk.api.access_token = "7425eedc7425eedc7425eedc65747258c4774257425eedc2db33deaf26b8661b14b86e8"
    # access_token='tocken'
    # session= vk.Session(access_token ='7425eedc7425eedc7425eedc65747258c4774257425eedc2db33deaf26b8661b14b86e8')
    vk_api = vk.API(session, v=5.73)
    # print(vk_api.checkToken(token=session.access_token,ip = ''))
    # wallKB = vk_api.wall.get(owner_id=-164236423)
    # print(wallKB['items'][1:])
    # text post_type post attachments date
    # a = vk_api.groups.getById(group_ids=152997613)
    temp = 1522778348
    while True:
        print('Start')
        wallKB = vk_api.wall.get(owner_id=-152997613)
        wall = wallKB['items'][1:]
        # date = openConfig(r'setting.ini')
        posts,dateVK = wallVkSendCurrentDate(wall,datetime.today())
        print(posts)
        if posts != []:
            temp = dateVK
            # date['Date'] = {'date':dateVK}
            # with open('setting.ini', 'w') as configfile:
            #     date.write(configfile)
            for post in posts[::-1]:
                a = "\n".join(post)
                print(a)
                try:
                    # pass
                    postToTelegram(a)
                except:
                    send_message(vk_api,46099694,'Обнови данные в телеграмме')
                    print('bedddd')
        else:
            print("We don't have update")
        t.sleep(3600)



