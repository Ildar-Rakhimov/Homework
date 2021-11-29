from pprint import pprint
import requests


def stackoverflow_request(link):
    response = requests.get(link).json()
    questions_list = []

    for element in response['items']:
        questions_list.append(element['title'])

    return questions_list


if __name__ == '__main__':
    url = 'http://api.stackexchange.com/2.3/questions?fromdate=1638057600&todate=1638144000&order=desc&sort=activity' \
          '&tagged=Python&site=stackoverflow'
    result = stackoverflow_request(url)
    pprint(result)