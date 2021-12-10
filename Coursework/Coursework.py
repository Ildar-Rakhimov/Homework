import os
import time
import json
import requests
from pprint import pprint

user_id = input('Введите id пользователя vk')
ya_token = input('Введите токен для Яндекс Диск')
photo_quantity = int(input('Сколько фотографий сохранить (предельное значение)?'))
url = 'https://api.vk.com/method/'

# Открываем токен для ВК
with open('token.txt', 'r') as file_object:
    vk_token = file_object.read().strip()


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

    def get_upload_link(self, path_to_file):
        """Метод для получения ссылки на загрузку"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file: str):
        """Метод для загрузки файла"""
        href = self.get_upload_link(path_to_file=path_to_file).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл загружен")


if __name__ == '__main__':
    resp = get_photo(vk_token, '5.131', user_id)
    json_list = []  # Список для json-файла с результатами
    likes_count = []  # Список для проверки количества лайков
    photo_counter = 0  # Счётчик для количества сохраняемых фотографий

    # Формируем имя папки и создаём локальную папку с таким именем
    dir_name = 'images' + time.strftime("%Y%m%d-%H%M%S")
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    uploader = YaUploader(ya_token)
    uploader.make_dir(dir_name)  # Создаём папку на Яндекс Диске

    for element in resp['response']['items']:
        if photo_counter < photo_quantity:

            temp_dict = {}  # Временный словарь для json-файла с результатами
            ava_url = element['sizes'][-1]['url']   # Ссылка на фото
            type_value = element['sizes'][-1]['type']  # Тип размера фото
            photo_name = element['likes']['count']  # Первоначальное имя фото из лайков

            # Если количество лайков одинаково, добавляем к имени фото дату загрузки
            if element['likes']['count'] in likes_count:
                photo_name = str(photo_name) + '_' + str(element['date']) + '.jpg'
            else:
                photo_name = str(photo_name) + '.jpg'

            # Добавляем значение лайков для фото в список для проверки
            likes_count.append(element['likes']['count'])

            # Обновляем временный словарь и добавляем его в json-файл
            temp_dict['size'] = type_value
            temp_dict['file_name'] = photo_name
            json_list.append(temp_dict)

            # Скачиваем фотографии
            r = requests.get(ava_url)
            with open(os.path.join(dir_name, photo_name), 'wb') as file:
                file.write(r.content)

            # Загружаем фотографии
            filename = os.path.join(dir_name, photo_name)
            path_to_file = dir_name + '/' + photo_name
            result = uploader.upload(path_to_file)

            photo_counter += 1
            print(f'Загружено фотографий: {photo_counter} из {photo_quantity}')

    # Записываем информацию в json-файл
    with open(os.path.join(dir_name, 'result.json'), 'w') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=2)
