from flask import render_template, url_for, redirect, flash, Markup
from app.models import User, Post
from . import auth
from .forms import LoginForm


@auth.route('/')
def index():
    user = User.query.all()
    if not user:
        return 'No user found'
    for name in user:
        user_details = {
            'Name': name.username, 'Email': name.email
        }
        return user_details.get('Email')
        # return user_details.get('Name')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            return redirect(url_for('auth.index'))
        flash(u'username or password is invalid', 'error')
    return render_template('login.html', form=form)
