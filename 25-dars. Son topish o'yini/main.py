# -*- coding: utf-8 -*-
"""
Using the module method
"""

# from son_top import findNumber
# findNumber(10)

# from son_top import findNumber as fn
# fn(10)

# import son_top
# son_top.findNumber(10)

# import son_top as st
# st.findNumber(10)

# from son_top import * 
# findNumber(10)

from son_top import findNumber , findNumberPc

def playGame(number):
    while True:
        game1 = findNumber(number)
        game2 = findNumberPc(number)
        
        if game1 < game2:
            print("\nFoydalanuvchi yutdi")
        elif game1 > game2:
            print('\nKomputer yutdi')
        else:
            print("O'yin durang hisobda yakunlandi ")
        takror = int(input('\nYana o\'ynashni hohlaysizmi? Ha(1)/Yo\'q(0)\n'))
        if takror == 0:
            break
playGame(10)
        