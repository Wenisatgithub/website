#! /usr/bin/python
# encoding utf-8

from flask import session
import os, stat

directory = {"default":"/home/default/"}

class user_directory():
    def get(self):
        if 'username' in session:
            user = session['username']
        else:
            user = "default"
        global directory
        return directory.get(user)

    def set(self, user):
        global directory
        if user:
            directory.update({user: "/home/" + user + "/"})
        else:
            directory.update({"default": "/home/default/"})

    def create(self, user):
        if user:
            path = "/home/" + user
        else:
            path = "/home/default"
        if not os.path.exists(path):
            os.mkdir(path)
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)