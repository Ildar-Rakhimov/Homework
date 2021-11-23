from pprint import pprint
import os


# Задание № 3: функция для объединения текстовых файлов

def join_txt_files(directory):

    # Формируем словарь

    files_list = os.listdir(directory)
    temp_dict = {}

    for file_name in files_list:
        if file_name.endswith(".txt"):
            with open(file_name, encoding="UTF-8") as f:
                data = f.readlines()
                temp_dict[file_name] = [len(data), data]

    # Создаем словарь с сортировкой

    sorted_values = sorted(temp_dict.values())
    sorted_dict = {}

    for element in sorted_values:
        for elem in temp_dict.keys():
            if temp_dict[elem] == element:
                sorted_dict[elem] = temp_dict[elem]

    # pprint(sorted_dict)

    # Записываем всё в новый файл

    with open('summary_file.txt', 'a', encoding="UTF-8") as file:
        for key, value in sorted_dict.items():
            file.write(key + '\n' + str(value[0]) + '\n')
            for el in value[1]:
                file.write(str(el).strip() + '\n')


join_txt_files(os.getcwd())