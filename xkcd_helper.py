import requests

from random import randint
from files_helper import get_extension_by_url, save_image_from_url


def download_xkcd_comics() -> tuple:
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    comics_number = randint(1, int(response.json()['num']))
    response = requests.get(f"https://xkcd.com/{comics_number}/info.0.json")
    response.raise_for_status()
    comics_data = response.json()
    comic_file_ext = get_extension_by_url(comics_data['img'])
    comic_file_name = f"{comics_number}{comic_file_ext}"
    save_image_from_url(comics_data['img'], comic_file_name)

    return comic_file_name, comics_data['alt']

