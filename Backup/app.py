import pprint
from flask import Flask , request

from wolf import search

import json
app = Flask(__name__)

@app.route('/')
def hello_workd():
    return 'Hello World'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        pp = pprint.PrettyPrinter(indent=3)
        data = request.json
        data_show = pp.pprint(data)
        
        text_fromline = data['events'][0]['message']['text']
        result =  search(text_fromline)
        
        print(result)

        from reply import ReplyMessage

        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Acess_Token='jk/JDjWTonRce6CZCdmBIhT8pzdR/HkKAMAlhPKHq6FMzZBoE2vkrWDMN5ZMvp2dDrWUfg+AViqVhqLobPr0ugQHklcAy0I+WDYTC+D/2mUE3Emt/5Ad9qybBDqoQhu8VSm40pYalA63a0pwL+QOfAdB04t89/1O/w1cDnyilFU='
        )

        return 'OK'
    elif request.method == 'GET':
        return "This is a get packate web page"
    else:
        return "NOT GET or PUT Method"

if __name__ == "__main__":
    app.run()

