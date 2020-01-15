from app import mail, redis_client
from threading import Thread
from flask_mail import Message
from flask import current_app, render_template

__author__ = '七月'


def do_send(app, msg, code, to):
    with app.app_context():
        try:
            mail.send(msg)
            key = "note:email:{}".format(to)
            redis_client.set(key, code, current_app.config['EXPIRE'])
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    msg = Message('[程序小样]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    t = Thread(target=do_send, args=[app, msg, kwargs["code"], to])
    t.start()
