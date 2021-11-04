# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:58:00 2021

@author: Dell
"""
""" 14-DARS. REVISION """

# otam = {'familiya':'karimov', 'ism':'shokir', 
# #         't_yil':1977,'t_sana':'16 sentabr','manzil':'parkent tumani'}
# onam = {'familiya':'salimova', 'ism':'mamura', 
# #         't_yil':1977,'t_sana':'24 iyun','manzil':'parkent tumani'}
# ukam = {'familiya':'payziyev', 'ism':'nurilloh', 
#         't_yil':2010,'t_sana':'28 mart','manzil':'parkent tumani'}

# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda, {otam['t_sana']}, {otam['manzil'].title()} da tavallud topgan")
# print(f"Onamning ismi {onam['ism'].title()}, {onam['t_yil']}-yilda, {onam['t_sana']}, {onam['manzil'].title()} da tavallud topgan")
# print(f"Ukamning ismi {ukam['ism'].title()}, {ukam['t_yil']}-yilda, {ukam['t_sana']}, {ukam['manzil'].title()} da tavallud topgan")

#1-way

# en_uz = {'apple':'olma', 'apricot':"o'rik", 'charry':'gilos'}
# user_input = input("English: ").lower()
# print(f"Uzbek: {en_uz[user_input]}")
#2-way

# en_uz = {'apple':'olma', 'apricot':"o'rik", 'charry':'gilos'}
# print('Uzbek :', end='')
# print(en_uz.get(user_input,'Bunday lug\'at mavjud emas '))

#3-way

en_uz = {'apple':'olma', 'apricot':"o'rik", 'charry':'gilos'}
en_uz['banana']='banan'
user_input = input("English: ").lower()
if user_input == None:
    print("Bunday so'z lu'gatda mavjud emas")
else:
    print(f"Uzbek: {en_uz[user_input]}")



