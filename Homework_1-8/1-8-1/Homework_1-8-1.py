from pprint import pprint
import os

# Задание № 1: формируем словарь с рецептами из файла

with open('recipes.txt', encoding="UTF-8") as file:
    cook_book = {}
    for recipe in file:
        dish_name = recipe.strip()
        count = int(file.readline().strip())
        temp_list = []
        for element in range(count):
            ingredient, quantity, measure = file.readline().split('|')
            item = {'ingredient_name': ingredient.strip(), 'quantity': quantity.strip(),
                    'measure': measure.strip()}
            temp_list.append(item)
        cook_book[dish_name] = temp_list
        file.readline()

# pprint(cook_book)


# Задание № 2: функция для формирования списка покупок

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for value in cook_book[dish]:
            if value['ingredient_name'] not in shop_list.keys():
                shop_list[value['ingredient_name']] = {'measure': value['measure'],
                                                       'quantity': int(value['quantity']) * person_count}
            else:
                shop_list[value['ingredient_name']]['quantity'] = (int(shop_list[value['ingredient_name']]['quantity'])
                                                                   + int(value['quantity']) * person_count)
    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Омлет'], 3))