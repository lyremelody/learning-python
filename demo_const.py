#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import const

const.PI = 3.14

my_pi = const.PI
print(my_pi)

try:
    const.PI = 3.14159
except const.ConstError as exp:
    print(exp)

try:
    del const.PI
except const.ConstError as exp:
    print(exp)

try:
    const.pi = 3.14
except const.ConstError as exp:
    print(exp)
