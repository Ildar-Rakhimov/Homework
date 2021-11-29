from pprint import pprint
import requests


def getting_url_list(char_list):
    """
    Формируем список адресов
    """
    url_list = []

    for hero in char_list:
        url_list.append("https://superheroapi.com/api/" + token + "/search/" + hero)

    return url_list


def getting_info(url_list):
    """
    Добавляем информацию из запросов в список
    """
    temp_list = []

    for url in url_list:
        resp = requests.get(url)
        temp_list.append(resp.json())

    return temp_list


def hero_int(hero_inf):
    """
    Формируем словарь с именем героя и значением интеллекта и выясняем, кто умнее
    """
    int_dict = {}

    for element in hero_inf:
        for key, value in element.items():
            if key == 'results':
                for elem in element[key]:
                    int_dict[elem['name']] = elem['powerstats']['intelligence']

    most_int_hero = None
    intellect_value = 0

    for key, value in int_dict.items():
        if intellect_value < int(value):
            most_int_hero = key
            intellect_value = int(value)

    return most_int_hero


if __name__ == '__main__':
    token = "2619421814940190"
    heroes_list = ['hulk', 'captain america', 'thanos']
    result = hero_int(getting_info(getting_url_list(heroes_list)))
    pprint(result)