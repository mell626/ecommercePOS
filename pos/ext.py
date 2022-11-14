from flask import *
from flask_sqlalchemy import *
from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import *
from flask_admin.contrib.sqla import ModelView
from flask_mail import *
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from werkzeug.utils import secure_filename
import os



db = SQLAlchemy()

mail = Mail()
