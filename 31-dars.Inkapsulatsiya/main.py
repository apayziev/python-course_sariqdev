# -*- coding: utf-8 -*-
"""
Main file
"""

from functions import Talaba

talaba1 = Talaba("Eshmat","Eshmatov","AB777777","1999",2)
talaba2 = Talaba("Mamarayim", "Mamatqulov", "AB8742777", 2000,2)
talaba3 =  Talaba("Mamatqul", "Mamajonov", "xxxxxxxx", 1998,3)
talaba1 = Talaba("Eshmat","Eshmatov","AB777777","1999")
talaba2 = Talaba("Mamarayim", "Mamatqulov", "AB8742777", 2000,2)
talaba3 =  Talaba("Mamatqul", "Mamajonov", "xxxxxxxx", 1998,3)

print(Talaba.get_talabar_soni())