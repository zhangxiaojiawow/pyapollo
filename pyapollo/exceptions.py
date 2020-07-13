#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/
# @Author  : Lin Luo/ Bruce Liu
# @Email   : 15869300264@163.com


class BasicException(BaseException):
    def __init__(self, msg: str):
        self._msg = msg
        print(msg)

    def __str__(self):
        return '%s: %s' % (self.__name__, self._msg)

class NameSpaceNotFoundException(BasicException):
    pass

class ServerNotResponseException(BasicException):
    pass
