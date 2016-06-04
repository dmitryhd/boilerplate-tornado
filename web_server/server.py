#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """
import tornado.ioloop
import tornado.web

PORT = 8888


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('a')


def get_app() -> tornado.web.Application:
    """ Sets up routing"""
    routing = [
        (r"/", IndexHandler),
    ]
    app = tornado.web.Application(routing)
    return app


def start_server():
    app = get_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    start_server()
