#coding:utf-8

import datetime
from peewee import *

MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'spider_system'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root.123'
mysql_db = MySQLDatabase(MYSQL_DBNAME, host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD)

class BaseModel(Model):
    class Meta:
        database = mysql_db


class Login(BaseModel):
    username = CharField(verbose_name='用户名', unique=True,
                         max_length=30)
    password = CharField(verbose_name='密码', max_length=128)

    class Meta:
        db_table = 'login'

class WebSite(BaseModel):
    '''
    需爬取的网站
    '''
    website = CharField(verbose_name='站点', unique=True,
                         max_length=30)
    create_time = DateTimeField(verbose_name='创建时间', default=datetime.datetime.now)

    class Meta:
        db_table = 'website'

class SearchKeyword(BaseModel):
    website = ForeignKeyField(WebSite)
    search_keyword = CharField(verbose_name='爬虫关键词', max_length=128)
    create_time = DateTimeField(verbose_name='创建时间', default=datetime.datetime.now)

    class Meta:
        db_table = 'search_keyword'
