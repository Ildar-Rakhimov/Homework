from Yandex_Disk import YaUploader
import unittest


with open('Yandex_token.txt', 'r') as file_object:
    ya_token = file_object.read().strip()

uploader = YaUploader(ya_token)


class TestYandex(unittest.TestCase):

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_make_dir(self):
        self.assertEqual(uploader.make_dir('test'), 201)
        print('Папка успешно создана')

    def test_make_dir_exist(self):
        self.assertEqual(uploader.make_dir('test'), 409)
        print('Такая папка уже существует')

    def test_make_dir_token(self):
        self.assertEqual(uploader.make_dir('test'), 401)
        print('Неверный токен')


if __name__ == '__main__':
    unittest.main()
