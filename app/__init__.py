# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from flask import Flask
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config.from_object('config')
#app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://root:123456@39.108.138.21:3306/test？charset=utf-8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
#Flask-OpenID扩展需要一个存储文件 的临时文件夹
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views,models

