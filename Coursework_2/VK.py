from pprint import pprint
import requests
import datetime
import random

user_id = 851877

def determine_age(birthday):
    """Функция для определения возраста по дате рождения"""
    age = (
                  datetime.date.today() - datetime.date(
                    int(birthday.split('.')[2]),
                    int(birthday.split('.')[1]),
                    int(birthday.split('.')[0])
                    )
          ).days // 365
    return age


# Считываем токены:
with open('VK_group_token.txt', 'r') as file_object:
    group_token = file_object.read().strip()

with open('VK_user_token.txt', 'r') as file_object:
    user_token = file_object.read().strip()


class VK_user:
    """Класс пользователя ВКонтакте"""
    def __init__(self, vk_group_token, vk_user_token):
        self.url = 'https://api.vk.com/method/'
        self.vk_group_token = vk_group_token
        self.vk_user_token = vk_user_token

    def list_of_cities(self):
        """Метод для получения списка городов России"""

        city_list = []
        # Задаём параметры
        list_of_cities_params = {
            'access_token': self.vk_user_token,
            'v': '5.131',
            'count': 1000,
            'country_id': 1,
            'need_all': 0
        }
        req = requests.get(self.url + 'database.getCities', params=list_of_cities_params).json()
        for element in req['response']['items']:
            city_list.append(element['title'].lower())

        return city_list

    def search_city(self, name):
        """Метод для получения id заданного города"""

        # Задаём параметры
        search_city_params = {
            'access_token': self.vk_user_token,
            'v': '5.131',
            'count': 1000,
            'country_id': 1,
            'need_all': 0,
            'q': name
        }
        req = requests.get(self.url + 'database.getCities', params=search_city_params).json()['response']['items'][0]
        found_city_id = req['id']

        return found_city_id

    def user_info(self, vk_user_id):
        """Метод для сбора информации о пользователе"""

        # Задаём параметры
        user_info_params = {
            'user_ids': vk_user_id,
            'access_token': self.vk_group_token,
            'v': '5.131',
            'fields': 'first_name, last_name, bdate, sex, city'
        }
        req = requests.get(self.url + 'users.get', params=user_info_params).json()['response'][0]

        # Словарь с данными пользователя:
        user_info_dict = {
            'user_id': user_id,
            'user_name': req['first_name'],
            'user_surname': req['last_name']
        }

        # Вычисляем возраст пользователя:
        if 'bdate' in req:
            user_info_dict['user_age'] = determine_age(req['bdate'])

        # Проверка на указание пола:
        if 'sex' in req:
            user_info_dict['user_sex'] = req['sex']

        # Проверка на указание города:
        if 'city' in req:
            user_info_dict['user_city'] = req['city']['id']

        pprint(user_info_dict)  # УДАЛИТЬ!

        return user_info_dict

    def search_for_pair(self, user_data):
        """Метод для поиска подходящих кандидатов"""

        # Пол партнёра по умолчанию:
        if user_data['user_sex'] == 1:
            pair_sex = 2
        elif user_data['user_sex'] == 2:
            pair_sex = 1
        else:
            pair_sex = 0

        # Задаём параметры поиска
        pair_params = {
            'access_token': self.vk_user_token,
            'v': '5.131',
            'count': 900,
            'city': user_data['user_city'],
            'age_from': user_data['user_age'] - 5,
            'age_to': user_data['user_age'] + 5,
            'status': 6,
            'sex': pair_sex,
            'fields': 'first_name, last_name, bdate, sex, city, relation, is_closed'
        }

        # Ищем кандидатов по указанным параметрам
        req = requests.get(self.url + 'users.search', params=pair_params).json()['response']['items']

        pairs_ids = []  # Список для id найденных кандидатов:

        # Добавляем открытые профили в список
        for element in req:
            if element['is_closed'] is False:
                pairs_ids.append(element['id'])

        candidate = random.choice(pairs_ids)  # Выбираем случайным образом кандидата из полученного списка людей

        # Задаём параметры для запрос информации о выбранном кандидате
        candidate_params = {
            'user_ids': candidate,
            'access_token': self.vk_group_token,
            'v': '5.131',
            'fields': 'first_name, last_name, bdate, sex, city, relation'
        }

        re = requests.get(self.url + 'users.get', params=candidate_params).json()['response'][0]

        # Создаём словарь с данными кандидата:
        candidate_info_dict = {
            'candidate_id': candidate,
            'candidate_name': re['first_name'],
            'candidate_surname': re['last_name'],
            'candidate_sex': re['sex']
        }

        # Вычисляем возраст кандидата:
        if 'bdate' in req:
            candidate_info_dict['candidate_age'] = determine_age(re['bdate'])

        if 'city' in req:
            candidate_info_dict['candidate_city'] = req['city']['id']  # Добавляем город в словарь

        pprint(candidate_info_dict)  # УДАЛИТЬ!

        return candidate_info_dict

    def getting_photos(self, person):
        """Функция для отбора фотографий кандидатов"""

        popularity_dict = {}  # Словарь для количества лайков и комментариев
        photo_id_dict = {}  # Словарь для id фотографий

        pair_params = {
            'access_token': self.vk_user_token,
            'v': '5.131',
            'owner_id': person['candidate_id'],
            'album_id': 'profile',
            'extended': 1
        }

        req = requests.get(self.url + 'photos.get', params=pair_params).json()

        # Заполняем словарь:
        for element in req['response']['items']:
            popularity_dict[element['sizes'][-1]['url']] = element['comments']['count'] + element['likes']['count']
            photo_id_dict[element['sizes'][-1]['url']] = element['id']

        # Отбираем три самые популярные фотографии:
        best_photos_list = sorted(popularity_dict, key=popularity_dict.get, reverse=True)[:3]

        best_photos_dict = {}  # Словарь для трёх лучших фотографий кандидата

        # Заполняем словарь:
        for elem in best_photos_list:
            best_photos_dict[elem] = popularity_dict.get(elem)

        photo_info_list = []  # Список с информацией о фотографиях для базы данных

        # Заполняем список:
        for key, value in best_photos_dict.items():
            photo_info_dict = {'photo_url': key, 'popularity': value, 'candidate_id': person['candidate_id']}
            for k, v in photo_id_dict.items():
                if key == k:
                    photo_info_dict['photo_id'] = v
            photo_info_list.append(photo_info_dict)

        return photo_info_list


if __name__ == '__main__':
    client = VK_user(group_token, user_token)

    result = client.getting_photos(client.search_for_pair(client.user_info(user_id)))
    pprint(result)
