#!/usr/bin/env Python
#coding:utf-8

import json

import tornado.web
from  tornado.escape import json_decode
from  tornado.escape import json_encode

from methods.models import Login

class LoginHandler(tornado.web.RequestHandler):

    template_name = "login.html"

    def get(self):
        self.render(self.template_name)

    def post(self):
        #import pdb
        #pdb.set_trace()
        print('body:{}'.format(self.request.body))
        data = json_decode(self.request.body)
        username = data["username"]
        password = data["password"]
        print("\033[96m login:{} \033[0m".format(username))
        if not Login.table_exists():
            Login.create_table()
        user, created = Login.get_or_create(username=username,
                                            defaults={
                                                'password': password
                                            })
        context = {
            'status': 200,
            'msg': 'OK'
        }
        ### 这里的数据前端接收不到，暂时不知道原因？
        #self.write(json.dumps(context))
        self.redirect('/index', status=301)
        #self.write(json.dumps(dict(
        #    location='/index'
        #)))

