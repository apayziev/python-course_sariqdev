# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 06:28:38 2021

@author: Dell
"""

"""AMALIYOT"""

#1)
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car =='gm':
#         print(car.upper())
#     else:
#         print(car.title())

#2)
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

#3)
# name = str(input(" Enter your login : "))
# if name == 'admin':
#     print("Xush kelibsiz, Admin\nFoydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {name.title()}!")

#5)
num = float(input("Enter the number : "))
# if num < 0:
#     print("Your number is negative")
# else:
#     print("Your number is positive.HaHa")
    
#6)
# if num > 0:
#     print((num ** (1/2)//1))
# else:
#     print("Please, enter positive number")
    
print(num**(1/2)) if num > 0 else print("Enter positive number ")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
print(f"Sonlar teng: {x}={y}") if x==y else print("Sonlar teng emas")