# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: microblog
# Name: microblog
# Author: mbegma
# Create data: 28.02.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------

# set FLASK_APP=microblog.py
# set FLASK_DEBUG=1
# flask run
# flask shell
# flask db migrate -m "new fields in user model" - создание миграции
# flask db upgrade - применение изменений миграции


from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_contex():
    return {'db': db, 'User': User, 'Post': Post}
