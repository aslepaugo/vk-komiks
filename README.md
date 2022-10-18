# XKCD comics in VK

This script publishes a random comics from [xkcd.com](https://xkcd.com/) on the wall in the VK community.

## Get started

We assume that you already have Python3 installed.

Use pip to install required dependencies.

```shell
pip install -r requirements.txt
```

To use the VK API follow instructions [here](https://vk.com/editapp?act=create).

Then get an access token [here](https://vk.com/dev/implicit_flow_user).

You will need the following access rights:  `photos, groups, wall, offline`.

Get your VK group id [here](https://regvk.com/id/).

Create file `.env` with the following environment variables.

```shell
VK_ACCESS_TOKEN=<vk_api_access_token>
VK_GROUP_ID=<community_id>
```

To run the script, type:

```shell
python main.py
```

After executing the script, you will receive a new post in the group.

![image](https://dvmn.org/filer/canonical/1567492781/267/)
