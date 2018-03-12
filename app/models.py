from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return 'username: {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def get_user(self):
        return User.query.get(self.user_id).username