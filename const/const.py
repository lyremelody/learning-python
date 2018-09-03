#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


class _Const(object):
    class ConstError(Exception):
        pass

    def __init__(self):
        _Const.__setattr__ = _Const._setattr_impl

    def _setattr_impl(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const {name}".format(name=name))

        if not name.isupper():
            raise self.ConstError("const name '{name}' is not all uppercase".format(name=name))

        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const instance attribute {name}".format(name=name))

        raise self.ConstError("Const instance has no attribute '{name}'".format(name=name))


sys.modules[__name__] = _Const()
