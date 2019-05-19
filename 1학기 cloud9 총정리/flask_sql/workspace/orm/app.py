from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User     # 다른 파일에서 모델을 가져와야 사용 가능
import os

app = Flask(__name__)

# flask app에 보낼 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'  # db 파일의 이름 설정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # True가 기본값인데,
# sqlalchemy DB 객체 수정 및 신호 방출 등을 추적하므로 과도한 메모리를 사용해 False


# sqlalchemy 초기화
# db = SQLAlchemy(app)   # 파일이 합쳐진 경우

db.init_app(app)   # 파일이 분리된 경우

migrate = Migrate(app, db)


@app.route('/')
# 뷰 함수(route 아래에 있는 함수)
def index():
    # url_for('index') =>>> '/'  view함수의 route를 return한다
    # return redirect(url_for('index'))
    users = User.query.all()   # <5> 입력한 정보를 모두 보여줌
    return render_template('index.html', users=users)    # index.html에서 정보를 받아와서 보여주기 위해 users를 넣음

@app.route('/users/create')   # orm 동작만 가능하게 하면 되므로 페이지는 필요 없다
def create():   # bootstrap을 적용해 바로 위에 글씨가 붙음
    username = request.args.get('username')   # <3>이 페이지에서 create 함수를 통해 username과 email로 정보가 들어감
    email = request.args.get('email')
    user = User(username=username, email=email)    # <4> DB에 넣으려고 함
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))   # 뷰 함수 이름을 url_for에 그대로 쓴다 -> 특별한 정보 페이지가 없다

@app.route('/users/delete/<int:id>')   # <2> 해당하려는 id만 지워야 한다
def delete(id):
    user = User.query.get(id)   # <3> id에 있는 정보를 지우고 db에 저장함 
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))   # <4> 메인 페이지로 리다이렉트한다


@app.route('/users/edit/<int:id>')   # <2> 몇 번 글인지를 알아야 한다
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)   # <3> 그 글에 입력된 정보를 수정 페이지에 보여준다

@app.route('/users/update/<int:id>')   # <6> 이제 바꾼 값을 저장해보자.
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')   # 수정된 값을 변수에 저장하기
    email = request.args.get('email')
    user.username = username
    user.email = email
    db.session.commit()   # update는 commit만 하면 된다
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)




