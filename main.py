import os
from random import randint
import requests
import urllib

from dotenv import load_dotenv
from files_helper import get_extension_by_url, save_image_from_url
from vk_api_helper import call_vk_method, publish_vk_wall_image
from xkcd_helper import get_comics_message, get_comics_url, get_last_comics_number


def main() -> None:
    load_dotenv()
    access_token = os.getenv('ACCESS_TOKEN')
    group_id = os.getenv('GROUP_ID')

    try:
        comic_image_id = randint(1, get_last_comics_number())
        comic_url = get_comics_url(comic_image_id)
        comic_message = get_comics_message(comic_image_id)
        comic_file_ext = get_extension_by_url(comic_url)
        comic_file_name = f"{comic_image_id}{comic_file_ext}"
        save_image_from_url(comic_url, comic_file_name)
    except requests.HTTPError as error:
        print('An error occuured while getting comics\n', error)
        return

    try:
        wall_upload_server = call_vk_method(method_name='photos.getWallUploadServer', access_token=access_token)
        upload_url = wall_upload_server['upload_url']
        publish_vk_wall_image(
            file_name=comic_file_name, 
            upload_url=upload_url, 
            access_token=access_token, 
            message=comic_message, 
            group_id=group_id
        )
    except requests.HTTPError as error:
        print('An error occuured while posting comics\n', error)
    finally:
         os.remove(comic_file_name)


if __name__ == '__main__':
    main()
