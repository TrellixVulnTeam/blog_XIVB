# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from hashlib import md5
from app import db
from app import models

import datetime

from flask_mail import Message


if __name__=='__main__':

    #db.drop_all()


    db.create_all()






    # admin_role = models.Role(name='Admin')
    # mod_role = models.Role(name='Moderator')
    # user_role = models.Role(name='User')
    #
    # user_john = models.User(username='john',role=admin_role)
    # user_susan = models.User(username='susan', role=user_role)
    # user_david = models.User(username='david', role=user_role)
    #
    # db.session.add(admin_role)
    # db.session.add(mod_role)
    # db.session.add(user_role)
    #
    # db.session.add(user_john)
    # db.session.add(user_susan)
    # db.session.add(user_david)
    #
    # db.session.commit()




    #
    # u = models.User(nickname='liubin', email='liubin@qq.com')
    #
    # db.session.add(u)
    # db.session.commit()

   #  #查询表中数据
   #  users = models.User.query.all()
   #
   #  for u in users:
   #
   #      print(u.id,u.nickname)
   #
   #  print(users)
   #
   #
   # #根据ID查询
   #  u = models.User.query.get(1)
   # #
   # #  print(u1)
   #
   #  p = models.Post(body='my first post!',timestamp=datetime.datetime.utcnow(), author=u)
   #
   #  db.session.add(p)
   #  db.session.commit()

    #清除数据
    #
    # user = models.User.query.all()
    #
    # for u in user:
    #
    #     db.session.delete(u)
    #
    # posts = models.Post.query.all()
    #
    # for p in posts:
    #
    #     db.session.delete(p)
    #
    #
    # db.session.commit()




