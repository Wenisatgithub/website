#!/usr/bin/python
# coding:utf-8

from flask import Blueprint
admin_bp  = Blueprint('admin',__name__, template_folder='templates',url_prefix='/admin')

@admin_bp.route('/')
def index():
    return "welcome to admin page!"