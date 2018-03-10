from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms.widgets import TextArea
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired('please enter you email'), Email()])
    password = PasswordField('Password:', validators=[DataRequired('please enter your password')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired('you username cannot be blank')])
    email = StringField('Email:', validators=[DataRequired('you email cannot be blank'), Email()])
    password = PasswordField('Password', validators=[DataRequired('please enter password')])
    confirm = PasswordField('Confirm password:', validators=[DataRequired('please enter confirm password'),
                                                             EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('username entered is currently in use')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email address is currently in use')


class AddPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired('this cannot be empty')])
    body = TextAreaField('Post', validators=[DataRequired('this cannot be empty')])
    submit = SubmitField('Add Post')
