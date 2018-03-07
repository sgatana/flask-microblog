from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return 'username {}'.format(User.username)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255))