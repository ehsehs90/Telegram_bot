from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id =config('CHAT_ID')



@app.route('/')
def hello_world():
    return 'HELLO WORLD'



@app.route('/write')
def write():
    return render_template('write.html')

    
@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '<h1>메세지전송완료</h1>'



# 텔레그램 서버가 우리 서버에게 HTTP POST 요청을 통해,
# 사용자 메시지 정보를 받아라고 전달해주는 것
@app.route('/{token}', methods=['POST'])
def telegram():
    return '', 200




if __name__=='__main__':
    app.run(debug=True)