#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

from handlers.index import IndexHandler
from handlers.login import LoginHandler


url = [
    (r'/login/?', LoginHandler),
    (r'/index/?', IndexHandler),
    (r'/index/crawler/?', IndexHandler.start_crawl()),
]
