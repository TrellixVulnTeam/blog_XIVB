# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from threading import Thread
from flask_mail import Message

from . import main
from .import  mail

from flask import render_template


def send_async_email(main, msg):

    with main.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, test_body):

    msg = Message(subject,sender=sender,recipients=recipients)

    msg.body = test_body
    # msg.html = html_body
    mail.send(msg)

def send_email1(to, subject, template, **kwargs):

    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASK_MAIL_SENDER'], recipients=[to])


    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)

    thr = Thread(target=send_async_email, args=[app, msg])

    thr.start()
    return thr
    #mail.send(msg)







