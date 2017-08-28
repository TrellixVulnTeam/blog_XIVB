# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@39.108.138.21:3306/test'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repositpry')

SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True

SECRET_KEY = 'you-will-never-guess'


OPENID_PROVIDERS = [

    {'name':'Google','url':'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo','url':'https://www.yahoo.com'},
    {'name':'AOL','url':'https://www.google.com/accounts/o8/id'},
    {'name':'Flockr','url':'https://www.Flockr.com/<username>'},
    {'name':'MyOpenID','url':'https://www.xxx.com/'}

]

