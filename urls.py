#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

from handlers.index import LoginHandler    #假设已经有了


url = [
    (r'/login/?', LoginHandler),
]
