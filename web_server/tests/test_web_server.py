#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from .. import server


class TestWebServer(unittest.TestCase):
    def test_server(self):
        app = server.get_app()
        self.assertTrue(app)


if __name__ == '__main__':
    unittest.main()
