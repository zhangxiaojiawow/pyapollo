#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/9/21
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from typing import Optional
from pyapollo.apollo_client import ApolloClient
from unittest import TestCase


class TestClient(TestCase):
    def test_client(self):
        obj = ApolloClient(app_id='bruce_test', config_server_url='http://106.54.227.205:8080')
        self.assertEqual(obj.get_value('a'), 'gogogogo123456')
        self.assertEqual(obj.get_value('c', '123'), '123')
        self.assertEqual(obj.get_value('c', '123', 'development.py-client'), '123')
