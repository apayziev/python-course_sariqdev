# -*- coding: utf-8 -*-
"""09-DARS. for TAKRORLASH OPERATORI"""

"""AMALIYOT"""

#1)
# ismlar = ['Gishmat','Toshmat','Eshmat','Mamatqul','Mamarayim']
# for ism in ismlar:
#     print(f"Xush kelibsiz - {ism}")
    
#2)
# print(f"Kod {len( ismlar)} marta takrorlandi")

#3)
# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")
    
#4)
# kinolar = []
# for kino in range(5):
#     kinolar.append(input(f"{kino+1}-kino : ")) 

# print(kinolar)

#4)

# suhbatlar_soni = int(input("Bugun nechta odam bilan suhbatda bo'ldingiz : "))
# insonlar = []
# print("uchrashgan odamlarning ismlarni birma bir kiriting")
# for inson in range(suhbatlar_soni):
#     insonlar.append(input(f"{inson+1} chi {input()} bilan uchrashdim : "))
# print(insonlar)

n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
    ismlar1 = str(ismlar)
print(ismlar1.title(), " - men bugun shular bn suhbatlashdim")