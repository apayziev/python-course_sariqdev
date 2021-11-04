# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 05:01:07 2021

@author: Dell
"""

"""14-DARS. lUG'AT BILAN TANISHUV"""

"""AMALIYOT"""

#1)
# Otam = {'ism':'Shokir','familiya':'Karimov','yoshi':'44'}
# Onam = {'ism':'Ma\'mura','familiya':'Salimova','yoshi':'44'}
# Ukam = {'ism':'Nurilloh','familiya':'Payziyev','yoshi':'11'}
# print(f"Otamning ismi {Otam['ism']}, familiyasi {Otam['familiya']}, yoshi {Otam['yoshi']} da")
# print(f"Onamning ismi {Onam['ism']}, familiyasi {Onam['familiya']}, yoshi {Onam['yoshi']} da")
# print(f"Ukamning ismi {Ukam['ism']}, familiyasi {Ukam['familiya']}, yoshi {Ukam['yoshi']} da")

#2)
# taomlar = {'Otam':'osh', 'Onam':'do\'lma', 'ukam':'shashlik'}
# print(f"Otamning sevimli taomi {taomlar['Otam']}")
# print(f"Onamning sevimli taomi {taomlar['Onam']}")
# print(f"Ukamning sevimli taomi {taomlar['ukam']}")

#3)
pyhton_variables = {'integer':'butun son saqlaydi','string':'matn saqlaydi',                   
                     'if':'shart bajaradi','float':'o\'nlik son saqlaydi'}
# print(f"Pythonda integer {pyhton_variables['integer']} ")
# print(f"Pythonda string {pyhton_variables['string']} ")

#4)
# print("Pythonga oid atamalarni kiriting!!!")
# user_input = str(input("So'zni kiriting : "))
# result = pyhton_variables.get(user_input,"Bunday so'z mavjud emas")
# print(result)

#5)
print("Pythonga oid atamalarni kiriting!!!")
user_input =str(input("Enter the word : "))
result = pyhton_variables.get(user_input)
if result == None:
    print("Bunday so'z mavjud emas")
else:
    print(result)