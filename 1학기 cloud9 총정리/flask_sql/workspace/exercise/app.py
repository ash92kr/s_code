from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'   # 어떤 파일을 만들 것인가
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # 추적 기능 끄기

# db에 app 연동
db.init_app(app)

# migrate 초기화
migrate = Migrate(app, db)
##################################### 헤더

@app.route('/')    # 순차적으로 만들기
def index():   # read
    users = User.query.all()   # 모든 테이블의 내용 가져오기
    return render_template('index.html', users=users)

# create/는 /을 붙이든 안 붙이든 접속 가능 = 라우팅 기능(/없이 엑세스하면 /있는 url로 잡아줌)
# create는 /를 안 붙여야만 접속 가능 = unique한 페이지 url
@app.route('/users/create/')
def create():
    nickname = request.args.get('nickname')   # request.form.get = post
    address = request.args.get('address')   # 변수 받기
    user = User(nickname=nickname, address=address)   # 왼쪽 변수가 컬럼명
    db.session.add(user)
    db.session.commit()   # 이제 db에 들어감
    return redirect(url_for('index'))   # 뷰 함수 이름을 직접 쓸 수 있다(라우팅 값이 아님)


@app.route('/users/delete/<int:id>/')
def delete(id):  # id 받아오기
    user = User.query.get(id)   # 하나만 가져오기
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/edit/<int:id>/')  # 페이지 보여주는 route
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)  # 그 페이지에 보여주기


@app.route('/users/update/<int:id>/')   # 바뀐 값을 모델에 저장하기
def update(id):
    user = User.query.get(id)
    nickname = request.args.get('nickname')
    address = request.args.get('address')   # edit.html의 form 이름
    
    user.nickname = nickname
    user.address = address
    db.session.commit()
    return redirect(url_for('index'))


##################################### footer
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)





