# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: microblog
# Name: __init__.py
# Author: mbegma
# Create data: 23.03.2018
# Description: blueprint для обработки ошибок
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
