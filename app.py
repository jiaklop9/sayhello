#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import url_for, flash, render_template, redirect

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash("You message have been send to the world!")
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
