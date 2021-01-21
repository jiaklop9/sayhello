#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from sayhello import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

BOOTSTRAP_SERVE_LOCAL = False  # True 使用本地bootstrap资源