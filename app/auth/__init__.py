# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: microblog
# Name: __init__.py
# Author: mbegma
# Create data: 26.03.2018
# Description: blueprint для авторизации
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
