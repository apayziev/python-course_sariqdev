# -*- coding: utf-8 -*-
"""
25-DARS. SON TOPISH O'YINI
"""
import random as rn

def findNumber(number):
    """Kompyueter foydalanuvchi o'ylagan sonni topuvchi dastur"""
    print('Game1\n')
    print(f"1 dan {number} gacha son o'yludim. Topa olasizmi? :")
    random_num = rn.randint(1, number)
    count = 0
    while True:
        count += 1
        number = int(input('Sonni kiriting : '))
        #sonni kompyuter o'ylagan son bilan tekshiradi  
        if random_num > number:
            print('Xato, men o\'ylagan son bundan kattaroq. Yana harakat qiling : ')
        elif random_num < number:
            print('Xato, men o\'ylagan son bundan kichikroq. Yana harakat qiling : ')
        elif random_num == number:
            print(f"\nCongrats (kim bo'sezam)👏. \nRostdan ham {random_num} ni o'ylagan edim."
                  f" {count} ta urinishda topdingiz.\nEee gap yog'uuu👍")
            break
    return count




def findNumberPc(number):
    """Foydalanuvchi o'ylagan sonni kompyuter topib beradi"""
    print('________________________________________________________________________')
    print('Game2\n')
    print(f"1 dan {number} gacha oraliqda bitta son o'ylang men topishga harakat qilaman")
    input('Sonnni o\'ylab boldingizmi? ENTER ni bosing: ')
    first_number = 1
    max_num = number
    count2 = 0
    
    while True:
        count2 += 1
        if first_number != max_num : 
            random_number = rn.randint(first_number, max_num)
        else :
            random_number = first_number
            
        user_input2 = input(f"Siz {random_number} ni o'yladingiz:\n"
                            f"To'g'ri bo'lsa (T) ni kiriting.\n"
                            f"Men o'ylagan son bundan kattaroq (+)\n"
                            f"Men o'ylagan son bundan kichikroq (-)\n")
      
        if user_input2 == '+':
            first_number = random_number + 1
        elif user_input2 == '-':
            max_num = random_number - 1
        else:
            break
    print(f"Men siz o'ylagan soni {count2} marta urinishda topdim. Uraaaa")
    return count2


        