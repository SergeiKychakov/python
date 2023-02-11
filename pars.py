import requests
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

HOST = 'https://www.eldorado.ru/'
URL = 'https://www.eldorado.ru/c/televizory/'
HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def parsing():

    url = "https://www.eldorado.ru/c/televizory/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")
    print(soup)
    data = soup.find("div")
    print(data)
    with open('time.txt', 'w', encoding='utf-8') as log:
        log.write(soup.text + '\n')


def main():
    html = get_html(URL)
    print(html)
    #parsing()

if __name__ == '__main__':
    main()