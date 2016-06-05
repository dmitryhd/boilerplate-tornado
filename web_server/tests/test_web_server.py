#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import json
from tornado.testing import AsyncHTTPTestCase

from .. import server

__author__ = "Dmitry Khodakov <dmitryhd@gmail.com>"


class TestWebServer(unittest.TestCase):
    def test_server(self):
        app = server.get_app()
        self.assertTrue(app)


class TestRequest(AsyncHTTPTestCase):
    def setUp(self):
        super(TestRequest, self).setUp()

    def get_app(self):
        return server.get_app()

    def fetch_html(self, url):
        resp = self.fetch(url)
        self.assertEqual(resp.code, 200)
        body = resp.body.decode('utf-8')
        return body

    def fetch_json(self, url):
        resp = self.fetch(url)
        self.assertEqual(resp.code, 200)
        body = resp.body.decode('utf-8')
        return json.loads(body)


class WebServerTest(TestRequest):
    def test_static(self):
        resp = self.fetch('/static/style.css')
        self.assertEqual(resp.code, 200)

    def test_page_render(self):
        body = self.fetch_html('/')
        self.assertIn('<!DOCTYPE html>', body)



class TestRest(TestRequest):
    def test_version(self):
        resp = self.fetch_json('/api/v1/version')
        self.assertEqual(resp['version'], '1.0')

    def test_other(self):
        resp = self.fetch_json('/api/v1/other')
        self.assertEqual(resp['other'], 0)

if __name__ == '__main__':
    unittest.main()
