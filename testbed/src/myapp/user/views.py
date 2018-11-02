#!/usr/bin/python
# coding:utf-8

from flask import request, session, render_template, url_for, redirect, Blueprint, flash, g
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from myapp.mysql import table
from myapp.user.user import user_directory

user_bp = Blueprint('user',__name__, template_folder='templates', static_folder='static')

class RegisteForm(FlaskForm):
    username = StringField(label=u'用户名', validators=[
                                            DataRequired(message = u'用户名不能为空'),
                                            Length(min=5, max=20, message = u'用户名长度需在5-20字符之间')])
    password = PasswordField(label=u'密码', validators=[
                                            DataRequired(message = u'密码不能为空'),
                                            Length(min=6, max=20, message = u'密码长度需在6-20字符之间')])
    repeatpwd = PasswordField(label=u'重复密码', validators=[
                                            EqualTo(fieldname = 'password', message= u'两次密码不匹配')])
    submit = SubmitField(u'注册')

@user_bp.route('/user_registe', methods=['GET','POST'])
def user_registe():
    form = RegisteForm()
    if request.method == 'POST' and form.validate():
        table_instance = table(g.db_ip, g.db_port, g.db_user, go.db_pwd, g.db_name, g.db_charset, g.db_table)
        if table_instance.query_user(form.username.data):
            flash(u'用户名已存在', 'danger')
        else:
            table_instance.add_user(form.username.data, form.password.data)
            user_dir = user_directory()
            user_dir.create(form.username.data)
            user_dir.set(form.username.data)
            flash(u'注册成功', 'success')
        table_instance.close_table()
    return render_template('user/user_LogReg.html', form=form)

class LoginForm(FlaskForm):
    username = StringField(label=u'用户名', validators=[
                                            DataRequired(message = u'用户名不能为空'),
                                            Length(min=5, max=20, message = u'用户名长度需在5-20字符之间')])
    password = PasswordField(label=u'密码', validators=[
                                            DataRequired(message = u'密码不能为空'),
                                            Length(min=6, max=20, message = u'密码长度需在6-20字符之间')])
    #rememberpwd = BooleanField(label=u'记住密码', default=False)
    submit = SubmitField(u'登录')

@user_bp.route('/user_login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        table_instance = table(g.db_ip,g.db_port, g.db_user, go.db_pwd, g.db_name, g.db_charset, g.db_table)
        if table_instance.query_user(form.username.data) and \
                                            table_instance.query_password(form.username.data) == form.password.data:
            session['username'] = form.username.data
            user_dir = user_directory()
            user_dir.set(form.username.data)
            flash(u'登陆成功', 'success')
        else:
            flash(u'用户名或者密码错误', 'danger')
        table_instance.close_table()
    return  render_template('user/user_LogReg.html',form=form)

@user_bp.route('/user_logout', methods=['GET', 'POST'])
def user_logout():
    session.pop('username',None)
    return redirect(url_for("user.user_login"))