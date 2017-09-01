# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


from flask import Blueprint

auth = Blueprint('auth', __name__)
from . import views

