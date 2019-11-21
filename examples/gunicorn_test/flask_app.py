#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : app
# @Time         : 2019-11-21 11:04
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run()
