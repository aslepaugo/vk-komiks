import os
from random import randint
import requests
import urllib

from dotenv import load_dotenv
from files_helper import get_extension_by_url, save_image_from_url
from vk_api_helper import call_vk_method, publish_vk_wall_image
from xkcd_helper import download_xkcd_comics


def main() -> None:
    load_dotenv()
    access_token = os.getenv('ACCESS_TOKEN')
    group_id = os.getenv('GROUP_ID')

    try:
        comic_file_name, comic_message = download_xkcd_comics()
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
