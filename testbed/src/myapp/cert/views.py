#!/usr/bin/python
# coding:utf-8

import commands
from flask import Blueprint, request, render_template
cert_bp  = Blueprint('cert',__name__, template_folder='templates')

@cert_bp.route('/view_cert', methods=['GET','POST'])
def view_cert():
    if request.method == 'GET':
        return render_template('cert/view_cert.html')
    else:
        cert_content = request.form.get('cert_content')
        #print cert_content
        cert_file = open('tmp.pem','w+')
        cert_file.write(cert_content)
        cert_file.close()
        cert_info = commands.getoutput("openssl x509 -in %s -text -noout" %('tmp.pem') )
        os.remove('tmp.pem')
        print cert_info
        return render_template('cert/view_cert.html', cert_info=cert_info)

@cert_bp.route('/create_cert', methods=['GET','POST'])
def create_cert():
    cert_dict = {"country":"","province":"","locality":"","organization":"","unit":"","emai":"","days":"","ip":"","dns":"","keylength":"","ca":""}
    if request.method == 'GET':
        return render_template('cert/create_cert.html')
    else:
        cert_dict['country'] = request.form.get('country')
        cert_dict['province'] = request.form.get('province')
        cert_dict['locality'] = request.form.get('locality')
        cert_dict['organization'] = request.form.get('organization')
        cert_dict['unit'] = request.form.get('unit')
        cert_dict['email'] = request.form.get('email')
        cert_dict['days'] = request.form.get('days')
        cert_dict['ip'] = request.form.get('ip')
        cert_dict['dns'] = request.form.get ('dns')
        cert_dict['keylength'] = request.form.get('keylength')
        cert_dict['ca'] = request.form.get('ca')
        for cert in cert_dict:
            print
        return render_template('cert/create_cert.html', result="ok")

@cert_bp.route('/sign_cert', methods=['GET','POST'])
def sign_cert():
    if request.method == 'GET':
        return render_template('cert/sign_cert.html')
    else:
        return render_template('cert/sign_cert.html', result="ok")