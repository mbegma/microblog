# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: microblog
# Name: __init__.py
# Author: mbegma
# Create data: 26.03.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes