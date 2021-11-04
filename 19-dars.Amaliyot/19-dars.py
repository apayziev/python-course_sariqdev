# -*- coding: utf-8 -*-
"""
19-DARS.FUNKSIYA
"""

"""AMALIYOTLAR"""

#1]

# name = input("Ismingizni  kiriting : ")
# year = int(input("Yoshingizni kiriting : "))
# def ismVaYosh(name, year):
#     print(f"{name.title()} was born in {2021 - year}. ")
# ismVaYosh(name, year)
# ismVaYosh('Eshmat', 19)

#2]

# def kvadratVaKub(num):
#     print(f"{num} soning kvadrati - {pow(num,2)}",
#           f"\n{num} soning kubi - {pow(num,3)}")
# kvadratVaKub(6)

#3]
# user_input = int(input('Enter the number : '))
# def evenOrOdd(user_input):
#     print("Your number is even") if user_input % 2 == 0 else print("Your number is odd")
# evenOrOdd(27)

#4]
# def compareTwoNums(num1, num2):
#     if(num1 > num2):
#         print(f"{num1} soni {num2} sonidan katta")
#     elif num1 == num2:
#         print("Sonlar teng")
#     else:
#         print(f"{num2} soni {num1} sonidan katta")
# compareTwoNums(-5, 9)
# compareTwoNums(9, 9)
# compareTwoNums(30, -8)

#5]
# def powerOfNums(x, y):
#     print(f"{x} sonining {y} darajasi = {pow(x, y)}")
# powerOfNums(5, -3)
# powerOfNums(-2, 3)

#6]
# def powerOfNums(x, y = 2):
#     print(f"{x} sonining {y} darajasi = {pow(x, y)}")
# powerOfNums(-9)

#7]
def result(x):
    for i in range(1, 11):
        if x % i == 0:
            print(i)
result(20)


