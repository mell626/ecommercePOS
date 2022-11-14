from ast import Pass
from pydoc import importfile
from .ext import *
from .models import *


class SignupForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(message='required')])
    confirm = PasswordField('Confirm Password: ', validators=[ DataRequired(message='required'), EqualTo('password', message='password mus match!')])


class LoginForm(FlaskForm):
    username = StringField('Username:', validators= [DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])