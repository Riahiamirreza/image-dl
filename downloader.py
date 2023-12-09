import sys

import requests
import bs4


def get_raw_page(query: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
    }
    params = {
        "q": query,
        "tbm": "isch",
    }

    response = requests.get("https://www.google.com/search", params=params, headers=headers)
    return response.text


def extract_image_links_from_raw_page(raw_page: str) -> list:
    bs = bs4.BeautifulSoup(raw_page, 'html.parser')
    breakpoint()
    return [i['src'] for i in bs.find_all('img')]

print(extract_image_links_from_raw_page(get_raw_page(sys.argv[1])))

