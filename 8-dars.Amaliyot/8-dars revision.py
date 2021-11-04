# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 06:23:32 2021

@author: Dell
"""

davlatlar = ['AQSH', 'Malasia', 'Turkey','UZB','Russia','Dubai','Qatar']
sorted(davlatlar)
print(sorted(davlatlar, reverse = True))
print(davlatlar)
print(sorted(davlatlar, reverse = False))
davlatlar.sort(reverse = True)
print(davlatlar)
sonlar = list(range(120,1200))
print(sonlar)
print(sum(sonlar))
print(max(sonlar) - min(sonlar))
print(len(sonlar))
print(sonlar[0:20])
print(sorted(sonlar[-20:],reverse = True))
print(sonlar[-20:])

taomlar = ['Manti', 'saryoq', 'somsa', 'tuxum', 'pirog']
nonushta = taomlar[:]
nonushta.remove('Manti')
nonushta.remove('somsa')
nonushta.append('choy')
nonushta.append('sir')
print(taomlar)
print(nonushta)
# nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'
nonushta = list(nonushta)
print(nonushta)

son = list(range(1,11))
print(sorted(son, reverse = True))

son_from = int(input("From : "))
son_to = int(input("To : "))
show = list(range(son_from,son_to))
print(show)





