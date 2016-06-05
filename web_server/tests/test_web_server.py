#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from tornado.testing import AsyncHTTPTestCase

from .. import server

__author__ = "Dmitry Khodakov <dmitryhd@gmail.com>"


class TestWebServer(unittest.TestCase):
    def test_server(self):
        app = server.get_app()
        self.assertTrue(app)


class RequestTest(AsyncHTTPTestCase):
    def setUp(self):
        super(RequestTest, self).setUp()

    def get_app(self):
        return server.get_app()


class WebServerTest(RequestTest):
    def static_test(self):
        resp = self.fetch('/static/style.css')
        self.assertEqual(resp.code, 200)

    def page_render_test(self):
        resp = self.fetch('/')
        self.assertEqual(resp.code, 200)
        body = resp.body.decode('utf-8')
        print(body)
        self.assertIn('<!DOCTYPE html>', body)


if __name__ == '__main__':
    unittest.main()
