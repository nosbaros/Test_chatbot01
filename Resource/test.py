import pprint
from flask import Flask , request

## from{ name of your file } import search
from wolf import search_wiki

app = Flask(__name__)

access_token = 'pmBXSjrmTke+bxiZYktLpg23mvLUiW9I9soRIZ+cpDztr54V3uMSbAZumW6H8mYzDrWUfg+AViqVhqLobPr0ugQHklcAy0I+WDYTC+D/2mWdLus40XvXYXieYBWEQIq4jcMUdg8XoCEP0Fn7e5YkMgdB04t89/1O/w1cDnyilFU='

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':

        pp = pprint.PrettyPrinter(indent=3)
        ### dictionary from line
        data = request.json
        data_show = pp.pprint(data)

        ## extract text from line
        text_fromline = data['events'][0]['message']['text']
        ## ค้นหาคำจาก wikipedia
        result = search_wiki(text_fromline)

        ### import function ในการส่งmessage reply.py
        from reply import ReplyMessage

        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Acees_Token = access_token
        )


        return 'OK'

    elif request.method == 'GET':
        return 'นี้คือลิงค์เว็บสำหรับรับ package'

if __name__ == "__main__":
    app.run(port=200)
