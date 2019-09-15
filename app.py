import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = '481c52b7720fcead640f9cdc29c22165'
channel_access_token = 'pmBXSjrmTke+bxiZYktLpg23mvLUiW9I9soRIZ+cpDztr54V3uMSbAZumW6H8mYzDrWUfg+AViqVhqLobPr0ugQHklcAy0I+WDYTC+D/2mWdLus40XvXYXieYBWEQIq4jcMUdg8XoCEP0Fn7e5YkMgdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    
        
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text)

    Reply_token = event.reply_token

    text_fromUSer = event.message.text
    # ### Set Text 
    # text_tosend_1 = TextSendMessage(text='Uncle Engineer 01',quick_reply=None)
    # text_tosend_2 = TextSendMessage(text='Uncle Engineer 02',quick_reply=None)

    # ### Set Image

    # image_message_1 = ImageSendMessage(
    #     original_content_url='https://image.shutterstock.com/image-vector/free-red-square-grunge-stamp-260nw-340650854.jpg'
    #     ,preview_image_url='https://www.webopedia.com/imagesvr_ce/8660/404-error.jpg'
    # )


    # line_bot_api.reply_message(
    #     Reply_token ,
    #     messages = [text_tosend_1 , text_tosend_2 , image_message_1]
    # )

    if 'เช็คราคา' in text_fromUSer:
        from Resource.bxAPI import GetBxPrice
        from random import randint
        num = randint(1,10)
        data = GetBxPrice(Number_to_get=num)

        from Resource.FlexMessage import setCarousel , setbubble

        flex = setCarousel(data)

        from Resource.reply import SetMenuMessage_Object , send_flex

        flex = SetMenuMessage_Object(flex)
        send_flex(Reply_token,file_data = flex,bot_access_key = channel_access_token)

    else:
        text_list = [
            'ฉันไม่เข้าใจที่คุณพูด กรุณาลองใหม่อีกครั้ง' ,
            'ขออภัย ฉันไม่เข้า่ใจ กรุณาลองใหม่อีกครั้ง' ,
            'ขอโทษค่ะ มีความหมายอย่างไงค่ะ กรุณาลองใหม่อีกครั้ง'
        ]

        from random import choice

        text_data = choice(text_list)

        text = TextSendMessage(text=text_data)
        line_bot_api.reply_message(Reply_token,text)

@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name

    botton_1 = QuickReplyButton(action=MessageAction(label='เช็คราครา',text='เช็คราคา'))
    botton_2 = QuickReplyButton(action=MessageAction(label='เช็คข่าวสาร',text='เช็คข่าวสาร'))

    qbtn = QuickReply(items=(botton_1,botton_2))

    text_1 = TextSendMessage(text='สวัสดีคุณ {} ยินดีตอนรับเข้าสู่บริการ Chatbot'.format(disname))
    text_2 = TextSendMessage(text='กรุณาเลือกสิ่งที่ต้องการ' , quick_reply = qbtn )

    line_bot_api.link_rich_menu_to_user(userid,'richmenu-e12a6e7f4b024f761c1d2557af3da26b')

    line_bot_api.reply_message(event.reply_token,messages=(text_1,text_2))


if __name__ == "__main__":
    app.run(port=200)