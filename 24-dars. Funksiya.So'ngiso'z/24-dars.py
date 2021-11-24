# -*- coding: utf-8 -*-
"""
24-DARS. FUNKSIYA. SO'NGI SO'Z

"""

# import math

#Nomsiz funkisiya bu - lambda

#aylananing uzunligini hisoblab beruvchi funksiya
# uzunlik = lambda pi, r: pi * r*2
# print(uzunlik((math.pi), 10))

# def aylanaUzunligi(pi, r):
#     return pi*r*2
# print(aylanaUzunligi(math.pi, 10 )) 
#--------------------------------------------------------------
#Sonning kvadratini hisoblash: 
# sonKvadrati = lambda a, b: a**b
# print(sonKvadrati(5, 2))

# def sonKvadrat(x, y):
#     return pow(x, y )
# print(sonKvadrat(5, 3))

# def daraja(n):
#     return lambda x: x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3 ning kvadrati {kvadrat(3)} ga, "
#       f"3 ning kubi {kub (3)} ga teng") 
#--------------------------------------------------------------
# from math import sqrt

# numbers = list(range(11))
# nums_sqrt = list(map(sqrt, numbers))
# print(nums_sqrt)

# def numsSqr(x):
#     return x*x

# print(list(map(numsSqr, numbers)))

# nums_sqrts = list(map(lambda x: x*x, numbers))
# print(nums_sqrts)
#--------------------------------------------------------------
import random as r

nums = r.sample(range(100), 10)
# print(nums)

# def isEven(x):
#     """This is a function to find whether even or odd"""
#     return x % 2 == 0
# even_nums = list(filter(isEven, nums))
# print(even_nums)

numss = [num for num in nums if num % 2 == 0]
print(numss)












