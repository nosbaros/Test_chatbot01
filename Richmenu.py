richdata = {
  "size": {
    "width": 2500,
    "height": 843
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": "เมนูหลัก",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 837,
        "height": 843
      },
      "action": {
        "type": "message",
        "text": "เช็คราคา"
      }
    },
    {
      "bounds": {
        "x": 850,
        "y": 8,
        "width": 807,
        "height": 816
      },
      "action": {
        "type": "message",
        "text": "เช็คข่าวสาร"
      }
    },
    {
      "bounds": {
        "x": 1682,
        "y": 8,
        "width": 808,
        "height": 825
      },
      "action": {
        "type": "postback",
        "text": "",
        "data": "ถามเรื่องทั่วไป"
      }
    }
  ]
}

from app import channel_access_token

import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):

    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())


CreateRichMenu(ImageFilePath='Resource/richmenu.jpeg',Rich_json=richdata,channel_access_token=channel_access_token)