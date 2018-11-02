#!/usr/bin/python
# coding:utf-8

### use Manager to run application, startup parameter is behind running command
from flask_script import Manager
from myapp import app

manager = Manager(app)
if __name__ == '__main__':
    manager.run()