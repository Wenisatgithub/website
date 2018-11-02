#!/usr/bin/python
# coding:utf-8
from flask import g
from myapp import app
@app.before_first_request
def db_init():
    g.db_ip = '10.74.53.141'
    g.db_port = 3306
    g.db_user = 'flask'
    g.db_pwd = 'flask'
    g.db_name = 'flask'
    g.db_charset = "utf8"
    g.db_table = "users"

# from run import manager
# @manager.option('-H','--db_ip', dest='db_ip')
# @manager.option('-P','--db_port', dest='db_port')
# @manager.option('-U','--db_user', dest='db_user')
# @manager.option('-K','--db_pwd', dest='db_pwd')
# @manager.option('-N','--db_name', dest='db_name')
# def get_args(db_ip,db_port,db_user,db_pwd,db_name):
#     pass
#

class ProductionConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'hard to guess string'

class DevelopmentConfig(object):
#   SERVER_NAME = "0.0.0.0:5000"
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'hard to guess string'

class TestingConfig(object):
    DEBUG = False
    TESTING = True