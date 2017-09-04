# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from flask import render_template,flash,redirect,session,url_for,request,g
from flask_login import login_user, logout_user,current_user,login_required
from ..models import User
from .forms import NameForm
from ..emails import send_email1
from . import main
from .. import db

from datetime import datetime


@main.route('/')

def index():

    return render_template('index.html')





