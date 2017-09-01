# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'liumeile0608@163.com'
    FLASKY_ADMIN = '183773928@qq.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):

    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USER_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')#liumeile0608@163.com
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')#891212kb
    MAIL_USERNAME = 'liumeile0608@163.com'
    MAIL_PASSWORD = '891212kb'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@39.108.138.21:3306/test'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@39.108.138.21:3306/test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@39.108.138.21:3306/test'


config = {

    'development':DevelopmentConfig,
    'testig':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}


#CSRF_ENABLED = True












