# -*- coding: utf-8 -*-
"""
AMALIYOT

"""

#4]

def is_fib_number(num):
    a = 0
    b = 1
    while b<num:
        a = b
        c = a+b
        b = c
    if b==num or a==num:
        return True
    if b > num:
        return False
