# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User',backref='role')

    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    # def is_anonymous(self):
    #     return False
    #
    # def get_id(self):
    #
    #     #return unicode(self.id) python2
    #     return str(self.id)
    

    def __repr__(self):
        return '<Roles %r>' % (self.name)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)



    username = db.Column(db.String(64),unique=True,index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):

        return '<User %r>' % (self.username)
