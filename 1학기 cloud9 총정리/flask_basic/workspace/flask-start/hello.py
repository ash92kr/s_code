from flask import Flask, render_template, request, url_for, redirect, flash
import random
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요 OOO입니다."
    
@app.route("/hello")    
def hello():
    return "짐이 묻건데 네 이름을 말하거라."
    
@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하심까? 신입사원 OOO입니다</h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1>여러 줄 보내기</h1>
    <ul>
        <li>쭉쭉쭉쭉 쭉쭉쭉쭉</li>
        <li>언제까지 어깨춤을</li>
        <li>추게할거야~</li>
        <li>내어깨를 봐</li>
        <li>탈골됐잖아</li>
    </ul>
    """
    
@app.route("/html_render")
def html_render():
    return render_template("index.html")


@app.route("/html_name/<string:name>/<float:age>/<int:money>/<path:time>")    
def html_name(name, age, money, time):
    return render_template("hello.html", your_name = name, your_age = age, your_money = money, your_time = time)
    
    
@app.route("/math/<int:num>")
def math(num):
    result = num**3
    result2 = num**5
    return render_template("math.html", my_num = num, result = result, result2 = result2)

@app.route("/dinner")
def dinner():
    list = ["편의점 도시락", "삼겹살", "간짜장", "집밥"]
    dict = {
        "편의점 도시락" : "http://news.tongplus.com/site/data/img_dir/2018/05/11/2018051101935_0.jpg",
        "삼겹살" : "http://cdn.jinfooduae.com/wp-content/uploads/2017/04/%EC%98%A4%EC%82%BC%EA%B2%B9%EC%82%B42-400x400.jpg",
        "간짜장" : "http://upload2.inven.co.kr/upload/2017/06/13/bbs/i15369150919.jpg",
        "집밥" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp3ACKaqsZK3w2cvOcpt_L6B2udYMf2BcdqcrFaRs80idFgf4p"
    }
    pick = random.choice(list)
    url = dict[pick]
    return render_template("dinner.html", pick = pick, url = url)
    
    
@app.route("/lotto")
def lotto():
    list = [i for i in range(1, 46)]   # list = list(range(1,46))
    pick = random.sample(list, 6)
    return render_template("lotto.html", pick = sorted(pick))
    
    
@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/daum")
def daum():
    return render_template("daum.html")
    
@app.route("/bing")
def bing():
    return render_template("bing.html")


@app.route("/ping")
def ping():
    return render_template("ping.html")
    
@app.route("/pong")
def pong():
    pingpong = request.args.get('ping')  # ping에서 입력한 값을 pingpong에 넣음
    return render_template("pong.html", pingpong = pingpong)


# opgg
# 1. id가 없는 경우
# 2. id가 있는데 tear(rank)가 없는 경우
# 3. id와 tear가 있는 경우

# 1. 소환사가 있는지 없는지, 있다면 승리수 출력
# 2. 소환사가 있으나 랭크전적이 없을 때

@app.route("/sohwan")
def sohwan():
    # req = requests.get("http://www.op.gg/summoner/userName={0}".format(id)).text 
    # soup = BeautifulSoup(req, 'html.parser')
    # rank = soup.select_one("#SummonerLayoutContent > div > div > div > div > div > div > span")
    return render_template("sowhan.html")   # 소환사가 있을 때


@app.route("/summoner")
def result():
    name = request.args.get('name')
    url = f"http://www.op.gg/summoner/userName={name}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser') 
    summoner = soup.select_one('body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header > div.Profile > div.Information > span')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    tier = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div > span')
    
    if summoner:
        if tier.text == "Unranked":
            flash(f"{name} 소환사는 랭크 전적이 없습니다.")
            # flash 메시지 보여주기 - 사이트 이름이 아니라 함수 이름을 적는다
            return redirect(url_for('sohwan'))
            # return render_template("notier.html", name=name)
        else:
            return render_template("opgg.html", name=name, wins=wins.text)
    else:
        flash(f"{name}을 가진 소환사가 없습니다.")
        # flash 메시지 보여주기
        return redirect(url_for('sohwan'))
        # return render_template("nouser.html", name=name)
        
    # id = request.args.get('opgg')
    # rank = request.args.get('opgg')
    # if type(id) == None:
    #     return render_template("result.html")
    # elif id not in None and type(rank) == None:
    #     return render_template("result2.html")
    # else:
    #     return render_template("result3.html")


if __name__ == "__main__":
    app.secret_key = "master_key"   # flask 문법에 따라 입력하면됨(""는 마음대로 입력)
    app.run(host="0.0.0.0", port=8080, debug=True)




    


