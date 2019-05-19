from flask import Flask, render_template, request, redirect
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import os
import csv
app = Flask(__name__)   # 인스턴스 만들기

@app.route('/')
def index():
    return 'hello there!'

# 5월 20일부터 d-day 카운트 출력하기
@app.route('/dday')
def dday():
    day = datetime(2019, 5, 20) - datetime.today()
    return f'{day.days}일 남았습니다.'
# https://docs.python.org/2/library/datetime.html#datetime.timedelta
# today = datetime.datetime.now()
# vacation = datetime.datetime(2019, 5, 20)
# td = vacation - today


# variable routing
# @app.route('/hi/<string:name>')
# def hi(name):   # 주소에 있는 것을 매개변수로 받아옴
#     return f'안녕, {name}'


@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number ** 3}입니다.'


# render template
# @app.route('/hi/<string:name>')
# def greeting(name):
#     # greeting.html로 위처럼 안녕 ~~를 출력하기
#     return render_template('greeting.html', html_name=name)
  
  
# if문
@app.route('/hi/<string:name>')
def greeting(name):
    # greeting.html로 위처럼 안녕 ~~를 출력하기
    return render_template('greeting.html', html_name=name)  


# for문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)
    
    
# fake google
@app.route('/google')
def google():
    return render_template('google.html')
    
    
@app.route('/ping')
def ping():
    pong = request.args.get('pong')
    return render_template('ping.html', pong_name=pong)
    

@app.route('/pong')
def pong():
    ping = request.args.get('ping')   # ping에서 입력한 내용을 받아옴
    # ping = request.args['ping']    # 이 방식으로 적어도 되나 키 값이 없다면 에러 발생함
    msg = request.args.get('msg')
    return render_template('pong.html', ping_name=ping, ping_msg=msg)    # pong.html에서 쓸 변수 = 방금 위의 것

    
# Post
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')
    
@app.route('/pong_new', methods=['POST'])   # methods로 받음
def pong_new():
    # name = request.form['name']
    name = request.form.get('name')   # post 방식은 args가 아니라 form을 적음
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)


# opgg
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
    
@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')   # 주의! request
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)


# 방명록
@app.route('/timeline')
def timeline():
    # username과 message 넘기기
    
    # 지금까지 기록된 방명록 보여주기(DictReader) - timeline.html의 form 아래 출력
    with open('timeline.csv', newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        dictionary = {}
        
        for row in reader:
            dictionary.update({row['username']: row['message']})
    
    return render_template('timeline.html', dictionary=dictionary)

    # timelines = []
    # with open('timeline.csv', 'r', newline='', encoding='utf-8') as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         timelines.append(row)
    # return render_template('timeline.html', timelines=timelines)


@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    # DictWriter 'timeline.csv' encoding fieldnames
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'username': username, 'message': message})

    # return render_template('timeline_create.html', username=username, message=message)
    return redirect('/timeline')



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)   # 자동으로 다른 환경에서 IP를 찾아줌