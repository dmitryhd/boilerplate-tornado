#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """
import os.path
import tornado.ioloop
import tornado.web as web


PORT = 8888

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'static/')


class IndexHandler(web.RequestHandler):
    def get(self):
        self.write('a')


def get_app() -> web.Application:
    """ Sets up routing"""
    routing = [
        (r"/", IndexHandler),
        (r"/static/(.*)", web.StaticFileHandler, {"path": STATIC_PATH}),
    ]
    app = web.Application(routing)
    return app


def start_server():
    app = get_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    print(STATIC_PATH)
    start_server()
