import os
import requests

from urllib.parse import urljoin


VK_API_HOST = "https://api.vk.com/method/"
VK_API_VERSION = "5.131"


def call_vk_method(method_name: str, access_token: str, method_params: dict={}):
    url = urljoin(VK_API_HOST, method_name)
    params = {
        "access_token": access_token,
        "v": VK_API_VERSION,
    }
    params = params | method_params
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    if 'error' in response.json():
        print(method_name, params)
        raise requests.HTTPError(response.json()['error']['error_msg'])
    
    return response.json()['response']


def publish_vk_wall_image(file_name: str, upload_url: str, access_token: str, message: str, group_id: int) -> None:
    with open(file_name, 'rb') as image:
        files = {
            'photo': image,
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        publish_settings = response.json()
    photo_save_params = {
        "server": publish_settings['server'],
        "photo": publish_settings['photo'],
        "hash": publish_settings['hash'],
    }
    response_save_photo = call_vk_method(
        method_name='photos.saveWallPhoto', 
        access_token=access_token, 
        method_params=photo_save_params
    )
    owner_id = response_save_photo[0]['owner_id']
    media_id = response_save_photo[0]['id']
    wall_post_params = {
        "owner_id": f"-{group_id}",
        "from_group": 1,
        "message": message,
        "attachments": f"photo{owner_id}_{media_id}",
    }
    call_vk_method(
        method_name='wall.post', 
        access_token=access_token, 
        method_params=wall_post_params
    )
