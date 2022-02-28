import unittest
from unittest.mock import patch
import main


class TestFirst(unittest.TestCase):

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_get_all_doc_owners_names(self):
        self.assertEqual(main.get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'})

    @patch('builtins.input')
    def test_get_doc_shelf(self, mock_input):
        mock_input.return_value = '10006'
        self.assertEqual(main.get_doc_shelf(), '2')

    @patch('builtins.input')
    def test_get_doc_owner_name(self, mock_input):
        mock_input.return_value = '11-2'
        self.assertEqual(main.get_doc_owner_name(), 'Геннадий Покемонов')

    @patch('builtins.input')
    def test_add_new_shelf(self, mock_input):
        mock_input.return_value = '4'
        self.assertEqual(main.add_new_shelf(), ('4', True))

    @patch('builtins.input')
    def test_delete_doc(self, mock_input):
        mock_input.return_value = '11'
        self.assertEqual(main.delete_doc(), None)


if __name__ == '__main__':
    unittest.main()
