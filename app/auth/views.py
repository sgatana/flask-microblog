from flask import render_template, url_for, redirect, flash, Markup, request
from app import db
from app.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from . import auth
from .forms import LoginForm, RegisterForm, AddPost


@auth.route('/', methods=['POST', 'GET'])
@login_required
def index():
    users = User.query.all()
    if not users:
        return 'No user found'
    posts = Post.query.filter_by(user_id=current_user.id)
    form = AddPost()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('post added', 'success')
        return redirect(url_for('auth.index'))
    print(form.errors)
    return render_template('index.html', form=form, users=users, posts=posts)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, You have been successfully registered')
        return redirect(url_for('auth.login'))
    print(form.errors)
    return render_template('register.html', form=form, title='Sign Up')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('auth.index')
            flash('you have successfully logged in', 'success')
            return redirect(next_page)
        flash(u'username or password is invalid', 'error')
    print('error', form.errors)
    return render_template('login.html', form=form, title='Sing In')


auth.route('/addPost')
def addPost():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = AddPost()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('post added', 'success')
        return redirect(url_for('auth.index'))
    return render_template('index.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been successfully logged out', 'success')
    return redirect(url_for('auth.login'))
