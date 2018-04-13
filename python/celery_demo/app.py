# coding=utf-8

import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, url_for, jsonify
from flask_mail import Mail, Message
from celery import Celery

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

app.config['MAIL_SERVER'] = 'smtp.domain.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'user@domain.com'
app.config['MAIL_PASSWORD'] = '123456'
app.config['MAIL_DEFAULT_SENDER'] = 'user@domain.com'

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'


mail = Mail(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def send_async_email(to, subject):
    msg = Message(subject, sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[to])
    msg.body = 'This is a test email sent from a background Celery task.'
    with app.app_context():
        mail.send(msg)


@celery.task(bind=True)
def long_task(self):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb), random.choice(adjective), random.choice(noun))
        self.update_state(state='PROGRESS', meta={'current': i, 'total': total, 'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!', 'result': 42}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email
    subject = "来自flask celery"

    if request.form['submit'] == '发送':
        send_async_email.delay(email, subject)
        flash('Sending email to {0}'.format(email))
    else:
        send_async_email.apply_async(args=[email, subject], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('index'))


@app.route('/longtask', methods=['POST'])
def longtask():
    task = long_task.apply_async()
    return jsonify({}), 202, {'Location': url_for('taskstatus', task_id=task.id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
