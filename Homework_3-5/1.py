import time

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def log_decorator(old_function):
    def new_function(*args, **kwargs):

        result = old_function(*args, **kwargs)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f'Дата и время вызова функции "{old_function.__name__}": {time.strftime("%d.%m.%Y-%H:%M:%S")}. '
                    f'Аргументы: {args, kwargs}, результат: {result}\n')

        return result
    return new_function


@log_decorator
def max_value_company(data):
    """Функция для определения сайта с наибольшими просмотрами"""

    max_count = 0
    company = ''

    for key, value in data.items():
        if value > max_count:
            max_count = value
            company = key

    return company


if __name__ == "__main__":

    max_value_company(stats)
