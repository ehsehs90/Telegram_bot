from flask import Flask, render_template, request
from decouple import config
import requests
import random

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
@app.route(f'/{token}', methods=['POST'])


def telegram():
 
     # 1. 메아리(Echo) 기능
     # 1.1 request.get_json() 구조 확인하기
     print(request.get_json())
     # 1.2 사용자 아이디, 텍스트 가져오기
     chat_id = request.get_json().get('message').get('from').get('id')
     text = request.get_json().get('message').get('text')
     # 1.3 텔레그램 API에게 요청을 보내서 답변해주기
     requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    # 1.2 사용자 아이디, 텍스트 가져오기

    #1. [기본] 로또 기능(random...?)

    # 사용자가 '/로또' 라고 말하면 랜덤으로 번호 6개 뽑아서 돌려주기!
    # 나머지 경우엔 전부 메아리 칩시다
   
     if(text =="/로또"):
        text=random.sample(range(1, 47), 6)
        
    
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')



    #2. [심화] vonvon 기능
    # 사용자가 '/vonvon 이름' 이라고 말하면 신이 나를 만들었을 때 요소 돌려주기!
     if text[0:8] == '/vonvon ' and len(text) >7 :
         user_name = text[9:]
         first_list=['힘','열정','체력']
         second_list=['오징어','꼴뚜기',"쭈꾸미"]
         texts =''
        
         texts += random.choice(first_list)
         texts += random.choice(second_list)
         text = texts
    
         requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


     return '', 200




if __name__=='__main__':
    app.run(debug=True)