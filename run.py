# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import os
from app import create_app,db
from app.models import User, Role
from flask_script import Manager, Shell

from flask_migrate import Migrate, MigrateCommand

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app,db = db, User = User,Role = Role)
manager.add_command("shell",Shell(make_context=make_shell_context))


#https://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask
manager.add_command('db',MigrateCommand)

if __name__=='__main__':

    manager.run()

