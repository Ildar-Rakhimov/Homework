import os
import time
import json
import requests
from pprint import pprint


def get_photo(token, version, id=None):
    """Функция для скачивания json файла с информацией о фотографиях"""
    photo_url = url + 'photos.get'
    photo_params = {
        'owner_id': id,
        'access_token': token,
        'v': version,
        'album_id': 'profile',
        'extended': 1
    }
    res = requests.get(photo_url, params=photo_params)
    return res.json()


class YaUploader:
    """Класс для загрузки файлов на Яндекс Диск"""
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        """Метод для получения заголовков"""
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def make_dir(self, path: str):
        """Метод для создания папки на Яндекс Диске"""
        dir_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.put(dir_url, headers=headers, params=params)
        return response.json()

    def upload_by_link(self, photo_url, path_to_file):
        """Метод для загрузки файла по url"""
        link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'url': photo_url, 'path': path_to_file}
        response = requests.post(link, headers=headers, params=params)
        return response.json()


if __name__ == '__main__':

    user_id = input('Введите id пользователя vk')
    ya_token = input('Введите токен для Яндекс Диск')

    url = 'https://api.vk.com/method/'

    # Открываем токен для ВК
    with open('token.txt', 'r') as file_object:
        vk_token = file_object.read().strip()

    try:
        quantity = int(input('Сколько фотографий сохранить (предельное значение)?'))
    except ValueError:
        print('Введено некорректное значение, сохраняем 5 фотографий')
        photo_quantity = 5
    else:
        photo_quantity = quantity

    resp = get_photo(vk_token, '5.131', user_id)
    json_list = []  # Список для json-файла с результатами
    likes_count = []  # Список для проверки количества лайков
    photo_counter = 0  # Счётчик для количества сохраняемых фотографий

    # Формируем имя папки
    dir_name = 'images' + time.strftime("%Y%m%d-%H%M%S")

    if 'error' in resp.keys():  # Проверка на ошибки доступа
        print('Не удалось скачать фотографии. Возможно, профиль закрыт.')
    elif 'response' in resp.keys():

        uploader = YaUploader(ya_token)  # Создаём экземпляр класса
        uploader.make_dir(dir_name)  # Создаём папку на Яндекс Диске

        for element in resp['response']['items'][:photo_quantity]:

            json_dict = {}  # Временный словарь для json-файла с результатами
            photo_name = element['likes']['count']  # Первоначальное имя фото из лайков

            # Если количество лайков одинаково, добавляем к имени фото дату загрузки
            if element['likes']['count'] in likes_count:
                photo_name = str(photo_name) + '_' + str(element['date']) + '.jpg'
            else:
                photo_name = str(photo_name) + '.jpg'

            # Добавляем значение лайков для фото в список для проверки
            likes_count.append(element['likes']['count'])

            # Обновляем временный словарь и добавляем его в json-файл
            json_dict['size'] = element['sizes'][-1]['type']
            json_dict['file_name'] = photo_name
            json_list.append(json_dict)

            # Загружаем фотографии
            path_to_file = dir_name + '/' + photo_name
            upload_resp = uploader.upload_by_link(element['sizes'][-1]['url'], path_to_file)
            photo_counter += 1
            if 'error' in upload_resp.keys():  # Проверка на ошибки
                print('Не валидный токен')
                break
            elif 'href' in upload_resp.keys():
                print(f'Загружено фотографий: {photo_counter}')

                # Записываем информацию в json-файл
                with open('result.json', 'w') as f:
                    json.dump(json_list, f, ensure_ascii=False, indent=2)
