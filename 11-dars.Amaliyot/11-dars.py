# -*- coding: utf-8 -*-
"""
11-DARS. BIR NECHTA SHARTLARNI TEKSHIRISH
"""

"""AMALIYOT"""

#1)

# num = int(input("Please, enter even number: "))
#1-way 
# print("Thank you") if num % 2==0 else print("Sorry , this is not even number")

#2-way
# if num%2:
#     print("Bu son juft emaas")
# else:
#     print("Rahmat")

#2)
# 1-way
# age = int(input("Enter your age : "))
# if age==4 or age>=60:
#     price=0
# elif age<18:
#     price=10000
# elif age>18:
#     price=20000
# print("Sizga kirish tekin") if price == 0 else print(f"Sizga kirish {price} so'm")

# 2-way
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

#3)
# a = float(input("Birinchi soni kiriting : "))
# b = float(input("Ikkinchi soni kiriting : "))

# if (a>b):
#     print(f"{a} soni {b} sonidan katta")
# elif (a<b):
#     print(f"{a} soni {b} sonidan kichik")
# else:
#     print("Siz kiritgan sonlar teng")

#4)

# mahsulotlar = ['olma', 'banan','pepsi', 'non', 'telefon', 'o\'yinchoq', 'arra','printer', 'maska', 'dori']
# savat = []
# mahsulotlar_soni = int(input("Nechta mahsulot kiritishni hohlaysiz ?\n"))
# for n in range(1,mahsulotlar_soni+1):
#     savat.append(input(f"{n}-chi mahsulotni kiriting : "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"\n{mahsulot.title()}-do'konimizda bor")
#     else:
#         print(f"\n{mahsulot.title()}-do'konimizda yo'q")

#5)
#1-way:
    
# mahsulotlar_base = ['olma', 'banan','pepsi', 'non', 'telefon', 'o\'yinchoq', 'arra','printer', 'maska', 'dori']
# siz_kiritgan_mahsulotlar = []
# bor_mahsulotlar = []
# mavjud_emas = []
#mahsulotlarni saralash jarayoni
# mahsulotlar_soni = int(input("Nechta mahsulot kiritishni hohlaysiz ?\n"))

# for mahsulot in range(1,mahsulotlar_soni+1):
#     siz_kiritgan_mahsulotlar.append(input(f"{mahsulot}-chi mahsulotni kiriting : "))

# for mahsulot in siz_kiritgan_mahsulotlar:
#     if mahsulot in mahsulotlar_base:
#         bor_mahsulotlar.append(mahsulot)
#     elif  mahsulot not in mahsulotlar_base:
#        mavjud_emas.append(mahsulot) 

#mavjud_emas ro'yxati elementlari:
# if mavjud_emas:
#         for n in range(1):
#             if (mahsulot in mavjud_emas) < 1:
#                 print("\nDo'konimizda quyidagi mahsulot mavjud emas:")
#                 for mahsulot in mavjud_emas:
#                     print(mahsulot)
#             else:
#                     print("\nDo'konimizda quyidagi mahsulotalar mavjud emas :")
#                     for mahsulot in mavjud_emas: print(mahsulot)
# else: print("Siz so'ragan barcha mahsulotlar do'konimizda mavjud")

#2-way:

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                # 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
#6)
#1-way:
# users = ['someone', 'luckyboy', 'hakker', 'sena', 'yamach']
# user = str(input("Please, enter your login here : "))
# if user.title() in users:
#     print("Bu login band, yangi login tanlang !")
# elif user not in users:
#     print(f"Xush kelibsiz, {user.title()}")

#2-way:
# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login.lower() in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

#7)
#1-way:
# num = int(input("Enter the number : "))
# for n in range(2,11):
#     if (num % n == 0):
#         print(f"{num} soni {n} ga qoldiqsiz bo'linadi")
#     else:
#         print(f"Ushbu oraliqda {num} soning bo'luvchilari yo'q")
  
#2-way:
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")










