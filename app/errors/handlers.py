# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: microblog
# Name: handlers
# Author: mbegma
# Create data: 23.03.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error/500.html'), 500