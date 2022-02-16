from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
substitution = r'+7 (\2) \3-\4-\5 \6 \7'


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

if __name__ == '__main__':

    # Формируем список контактов с правильным распределением элементов по записям
    people_list = list()
    for element in contacts_list:
        new_name = ' '.join(element[:3]).split(' ')
        element[5] = re.sub(pattern, substitution, element[5])
        new_person = [new_name[0], new_name[1], new_name[2], element[3], element[4], element[5], element[6]]
        people_list.append(new_person)

    # Формируем список контактов без повторяющихся записей

    fixed_info_list = []
    for i in range(len(people_list)):
        for j in range(len(people_list)):
            if people_list[i][:2] == people_list[j][:2]:
                people_list[i] = [x or y for x, y in zip(people_list[i], people_list[j])]
        if people_list[i] not in fixed_info_list:
            fixed_info_list.append(people_list[i])
    fixed_info_list.sort()
    people_list = fixed_info_list

    pprint(people_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(people_list)