#!/usr/bin/env Python
#coding:utf-8

import json

import tornado.web
from  tornado.escape import json_decode
from  tornado.escape import json_encode

from methods.models import WebSite, SearchKeyword

class IndexHandler(tornado.web.RequestHandler):
    template_name = 'index.html'

    def __init__(self, application, request, **kwargs):
        super(IndexHandler, self).__init__(application, request, **kwargs)
        if not WebSite.table_exists():
            WebSite.create_table()
        if not SearchKeyword.table_exists():
            SearchKeyword.create_table()

    def get(self):
        website = WebSite.select()
        sites = [ web.website for web in website]
        self.render(self.template_name, sites=sites)

    @staticmethod
    def start_crawl(self):
        #import pdb
        #pdb.set_trace()
        print('body:{}'.format(self.request.body))
        data = json_decode(self.request.body)
        website = data["website"]
        keyword = data["keyword"]
        print("\033[96m login:{} \033[0m".format(website))
        context = {
            'status': 200,
            'msg': 'OK'
        }
        ### 这里的数据前端接收不到，暂时不知道原因？
        self.write(json.dumps(context))
        #self.write(json.dumps(dict(
        #    location='/index'
        #)))


