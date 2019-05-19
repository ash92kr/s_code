from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # DB 초기화

class User(db.Model):  # DB를 하나의 class로 본다
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    # id열은 숫자이며, 기본키
    username = db.Column(db.String(80), unique=True, nullable=False)
    # username열은 80자 이내의 문자열만 들어가며, 중복될 수 없고, null값이 불가능함
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User '{self.username}'>"   # 무엇이 설치되었는지 보여줌
