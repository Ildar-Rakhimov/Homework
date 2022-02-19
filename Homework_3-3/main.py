import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
base_url = 'https://habr.com'


def search_habr(heads, keys, url):
    """Функция для отбора статей с Хабра по ключевым словам"""
    response = requests.get(url + '/ru/all/', headers=heads)
    response.raise_for_status()
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    found_articles = list()  # Список для хранения результатов

    for article in articles:
        hubs = article.find_all(class_='tm-article-snippet')
        hubs = list(hub.text.strip() for hub in hubs)
        for hub in hubs:
            for word in keys:
                if word in hub:
                    href = article.find(class_="tm-article-snippet__readmore").attrs['href']  # Ссылка на полный текст
                    title = article.find(class_="tm-article-snippet__title-link").text  # Заголовок статьи
                    date = article.find(class_="tm-article-snippet__datetime-published").text  # Дата публикации
                    result = date + ' - ' + title + ' - ' + url + href  # Элементы списка
                    found_articles.append(result)  # Добавляем элементы в список

    return found_articles


if __name__ == '__main__':
    print(search_habr(HEADERS, KEYWORDS, base_url))
