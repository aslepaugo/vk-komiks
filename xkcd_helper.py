import requests


def get_last_comics_number() -> int:
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    return int(response.json()['num'])


def get_comics_url(comics_number: int) -> str:
    url = f"https://xkcd.com/{comics_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['img']


def get_comics_message(comics_number: int) -> str:
    url = f"https://xkcd.com/{comics_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['alt']
