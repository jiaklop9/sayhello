#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import flash
from sayhello import app, db


@app.cli.command("init_db")
def init_db():
    """db.drop_all()-->db.create_all()"""
    db.drop_all()
    db.create_all()