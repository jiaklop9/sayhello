#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    """
    timestamp字段的默认值是datetime.now而不是datetime.now（）。
    前者是可调用的函数 / 方法对象（即名称），
    而后者是函数 / 方法调用（即动作）。
    SQLAlchemy会在创建新的数据库记录时（即用户提交表单实例化Message类时）调用该对象来设置默认值，这也是我们期待的效果。
    如果传入的不是方法对象，那么这个方法在加载模块时就会被执行，这将不是正确的时间戳。
    """
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)