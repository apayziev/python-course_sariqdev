# -*- coding: utf-8 -*-
"""
AMALIYOT
"""

#2]

def kattaHarf(): 
    with open('matn_1.txt') as txt_file:
        file = txt_file.read()
    return file[0].title() + file[1:]
print(kattaHarf())

def matn_2():
    with open('matn_1_.txt') as text_file:
        return text_file.read()