from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired('please enter you email')])
    password = PasswordField('Password:', validators=[DataRequired('please enter your password')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


