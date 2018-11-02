#!/usr/bin/python
# coding:utf-8

#### import flask framework ######
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

#### blueprint register #######
from myapp.cert.views import cert_bp
from myapp.file.views import file_bp
from myapp.user.views import user_bp
from myapp.admin.views import admin_bp

app.register_blueprint(cert_bp)
app.register_blueprint(file_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

#### import front-end framework #######
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

#### init configuration #########
from myapp.setting import DevelopmentConfig
app.config.from_object(DevelopmentConfig)

#### application homepage ########
@app.route('/')
def index():
    return render_template("base.html")