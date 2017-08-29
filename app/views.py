# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from flask import render_template,flash,redirect,session,url_for,request,g
from flask_login import login_user, logout_user,current_user,login_required
from app import app,lm,db,oid
from .models import User
from .forms import LoginForm



# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))
#
# @app.before_request
# def before_request():
#     g.user = current_user
#
#
# @app.route('/login',methods=['GET','POST'])
# @oid.loginhandler
# def login():
#
#     if g.user is not None and g.user.is_authenticated:
#
#         print(g.user)
#
#         return redirect(url_for('index'))
#
#     form = LoginForm()
#
#     if form.validate_on_submit():
#
#         session['remember_me'] = form.remember_me.data
#         # flash('Login requested for OpenID= "' + form.openid.data + '",remember_me = ' + str(form.remember_me.data))
#         return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
#     return  render_template('login.html',
#                             title='Sign In',
#                             form = form,
#
#                             providers = app.config['OPENID_PROVIDERS'])
#
# @oid.after_login
# def after_login(resp):
#
#     if resp.email is None or resp.email == "":
#         flash('Invalid login. please try again.')
#
#         return redirect(url_for('login'))
#     user = User.query.filter_by(email=resp.email).first()
#
#     if user is None:
#
#         nickname = resp.nickname
#
#         if nickname is None or nickname == "":
#
#             nickname = resp.email.split('@')[0]
#             user = User(nickname=nickname,email=resp.email)
#
#             db.session.add(user)
#             db.session.commit()
#
#     remember_me = False
#
#     if 'remember_me' in session:
#         remember_me = session['remember_me']
#         session.pop('remember_me', None)
#     logout_user(user,remember = remember_me)
#     return  redirect(request.args.get('next')) or url_for('index')
#
#
# @app.route('/logout')
# def logout():
#
#     logout_user()
#     return redirect(url_for('index'))

@app.route('/')
@app.route('/index')

def index():
    user_agent = request.headers.get('User-Agent')

    return '<h1>You browser is %s </h1>' % user_agent

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


#自定义错误页面
@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):

    return render_template('500.html'),500


# @app.route('/user/<nickname>')
# @login_required
# def user(nickname):
#
#     user = User.query.filter_by(nickname=nickname).first()
#     if user == None:
#
#         flash('User ' + nickname + ' not found..')
#
#
#         return redirect(url_for('index'))
#
#     posts = [
#         {'author':user, 'body':'test post #1'},
#         {'author':user, 'body': 'test post #2'}
#
#     ]
#
#     return render_template('user.html',
#                            user = user,
#                            posts = posts)

