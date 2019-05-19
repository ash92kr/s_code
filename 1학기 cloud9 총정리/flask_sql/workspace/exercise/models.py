from flask_sqlalchemy import SQLAlchemy

# sqlalchemy 초기화
db = SQLAlchemy()

# sqlalchemy datatype
# Integer / String(길이) / Text / DateTime / Float / Boolean
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)   # nullable=False여도 빈 string 값은 입력됨
    





