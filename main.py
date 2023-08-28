import json

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.mongodb.com/careers/positions"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    js = json.loads(soup.find("script", {'id': 'data-grnhs'}).text)
    for job in js['jobs']:
        data={
            'id': job['id'],
            'title': job['title'],
            'location': job['location'],
            'department': job['department'],
        }
        print(data)


if __name__ == '__main__':
    main()
