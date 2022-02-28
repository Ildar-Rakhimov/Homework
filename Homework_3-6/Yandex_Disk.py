import requests
import time

with open('Yandex_token.txt', 'r') as file_object:
    ya_token = file_object.read().strip()


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

    def make_dir(self, path):
        """Метод для создания папки на Яндекс Диске"""
        dir_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.put(dir_url, headers=headers, params=params)
        return response.status_code


if __name__ == '__main__':
    uploader = YaUploader(ya_token)  # Создаём экземпляр класса
    uploader.make_dir(time.strftime("%d.%m.%Y - %H.%M.%S"))  # Создаём папку на Яндекс Диске