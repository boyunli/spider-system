#!/usr/bin/env Python
# coding=utf-8

from urls import url

import tornado.web
import os


settings = dict(
    debug = True,
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
    )

application = tornado.web.Application(
    handlers = url,
    **settings
    )

