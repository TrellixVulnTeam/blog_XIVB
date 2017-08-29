# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from hashlib import md5
from app import db
from app import models

import datetime

if __name__=='__main__':

    #db.drop_all()
    # db.create_all()

    u = models.User(nickname='liubin', email='liubin@qq.com')

    db.session.add(u)
    db.session.commit()

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
    u = models.User.query.get(1)
   #
   #  print(u1)

    p = models.Post(body='my first post!',timestamp=datetime.datetime.utcnow(), author=u)

    db.session.add(p)
    db.session.commit()

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




