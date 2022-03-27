from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import VK
import database as db
from pprint import pprint
import requests
import re

# Считываем токены:
with open('VK_group_token.txt', 'r') as file_object:
    group_token = file_object.read().strip()

with open('VK_user_token.txt', 'r') as file_object:
    user_token = file_object.read().strip()

client = VK.VK_user(group_token, user_token)  # Создаём экземпляр класса
session = requests.Session()
vk = vk_api.VkApi(token=group_token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    """Функция для отправления сообщений"""
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7)})


def send_image(photo_dict):
    """Функция для отправки фотографий кандидата"""
    attachment_list = []
    for item in photo_dict:
        attachment_list.append('photo' + str(item['candidate_id']) + '_' + str(item['photo_id']))
    for number, element in enumerate(attachment_list, 1):
        vk.method('messages.send', {'peer_id': event.user_id,
                                    'message': f"Фотография кандидата № {str(number)} из {str(len(attachment_list))}",
                                    'attachment': element,
                                    'random_id': 0}
                  )

    return attachment_list


# Логика чат-бота:
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            client_info = client.user_info(event.user_id)
            # db.insert_user(client_info)  # Записываем данные пользователя в базу данных
            city_list = client.list_of_cities()
            request = event.text.lower()
            if request == 'привет':
                if len(client_info) == 6:
                    write_msg(event.user_id, f'Здравствуйте! Введите слово \"поиск\" для запуска программы.')
                elif len(client_info) != 6:
                    if 'sex' not in client_info:
                        write_msg(event.user_id, 'Для определения вашего пола введите \"ж\" или \"м\"')
                    elif 'city' not in client_info:
                        write_msg(event.user_id, 'Введите название вашего города. ')
                    elif 'age' not in client_info:
                        write_msg(event.user_id, 'Введите дату вашего рождения в формате ДД.ММ.ГГГГ')
            elif request in city_list:
                client_info['user_city'] = client.search_city(request)
                write_msg(event.user_id, 'Город введён. Введите слово \"поиск\" для запуска программы.')
            elif request == 'ж':
                client_info['user_sex'] = 1
                write_msg(event.user_id, 'Пол введён. Введите слово \"поиск\" для запуска программы.')
            elif request == 'м':
                client_info['user_sex'] = 2
                write_msg(event.user_id, 'Пол введён. Введите слово \"поиск\" для запуска программы.')
            elif request == re.match(r'[0-3]\d\.[0-1]\d\.[1-2]\d\d\d', request):
                client_info['user_sex'] = VK.determine_age(request)
                write_msg(event.user_id, 'Дата рождения введена. Введите слово \"поиск\" для запуска программы.')
            elif request == 'пока':
                write_msg(event.user_id, 'До свидания!')
            elif request == 'поиск':
                write_msg(event.user_id, 'Запущен поиск пары...')
                b = (client.search_for_pair(client_info))
                # db.insert_candidate(b)  # Записываем кандидата в базу данных
                result = client.getting_photos(b)
                # db.insert_photo(result)  # Записываем фотографии в базу данных
                write_msg(event.user_id,
                          f"Найден кандидат: https://vk.com/id{result[0]['candidate_id']}. Отправляем популярные "
                          f"фотографии...")
                send_image(result)

            else:
                write_msg(event.user_id, 'Команда не распознана. Введите слово \"поиск\" для запуска программы.')