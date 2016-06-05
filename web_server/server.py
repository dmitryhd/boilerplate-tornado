#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.ioloop
import tornado.web as web

__author__ = "Dmitry Khodakov <dmitryhd@gmail.com>"


PORT = 8888

APP_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(APP_PATH, 'static/')
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')


class IndexHandler(web.RequestHandler):
    def get(self):
        # self.write('aaa')
        self.render('index.html')


def get_app() -> web.Application:
    """ Sets up routing"""
    routing = [
        (r"/", IndexHandler),
        (r"/static/(.*)", web.StaticFileHandler, {"path": STATIC_PATH}),
    ]
    app = web.Application(routing)
    app.settings['template_path'] = TEMPLATE_PATH
    return app


def start_server():
    app = get_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    start_server()
