import requests

from os.path import splitext
from urllib.parse import urlsplit


def save_image_from_url(source_url: str, destination: str) -> None:
    response = requests.get(source_url)
    response.raise_for_status()
    with open(destination, "wb") as file:
        file.write(response.content)


def get_extension_by_url(url: str) -> str:
    path = urlsplit(url).path
    extension = splitext(path)[1]
    return extension
