nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    """Класс для первого задания (итератор)"""

    def __init__(self, data_list):
        self.data_list = data_list
        self.cursor = 0
        self.inner_cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.inner_cursor < len(self.data_list[self.cursor]) - 1:
            self.inner_cursor += 1
            return self.data_list[self.cursor][self.inner_cursor]
        else:
            self.inner_cursor = 0
            self.cursor += 1
            if self.cursor == len(self.data_list):
                raise StopIteration
        return self.data_list[self.cursor][self.inner_cursor]


def flat_generator(data):
    """Функция для второго задания (генератор)"""

    for value in data:
        for element in value:
            yield element


if __name__ == "__main__":

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print('\n --- Разделитель --- \n')

    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)

