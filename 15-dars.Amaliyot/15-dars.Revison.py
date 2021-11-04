# -*- coding: utf-8 -*-
"""
15-DARS. REVISON
"""

#1]
# python_termins = {'integer':'butun son saqlaydi',
#                   'double':"o'nlik son saqlaydi",
#                   'if':'shart bajarish operatori',
#                   'boolean':'mantiqiy amal bajarish operatori',
#                   'float':'butun bo\'lmagan sonlarni saqlaydi',
#                   'string':'matn saqlaydi',
#                   'input':'foydalanuvchidan qiyat oladi',
#                   'for':'sikl bajaradi'
#                   }
# for key,value in sorted(python_termins.items()):
#     print(f"{key.title()} - {value}")

#2]
# python_termins = {'integer':'butun son saqlaydi',
#                   'double':"o'nlik son saqlaydi",
#                   'if':'shart bajarish operatori',
#                   'boolean':'mantiqiy amal bajarish operatori',
#                   'float':'butun bo\'lmagan sonlarni saqlaydi',
#                   'string':'matn saqlaydi',
#                   'input':'foydalanuvchidan qiyat oladi',
#                   'for':'sikl bajaradi'
#                   }    
# print("Lug'atda mavjud terminlar: ")
# for key in sorted(python_termins.keys()):
#     print(key.upper())
# print("Lug'atlarga tariflar : ")
# for value in sorted(python_termins.values()):
#     print(value)

#3]

#1-way:
    
# user_input = input('Pythonga oid atamalarni kiriting: ').lower()
# if user_input not in python_termins.keys():
#     print("Bazada bunday atama mavjud emas")
# else:
#     print(f"{(user_input).title()} - {python_termins[user_input]}")

#2-way:
    
# print(f"{python_termins.get(input('Atamani kiriting : '),'Bazada bunday atama mavjud emas')}")

#3-way:
    
# result = python_termins.get(input("Atamani kiriting : "))
# if result == None:
#       print('Bazada bunday so\'z mavjud emas ')
# else:
#       print(f"{result}")

#4]

# taomlar_royxati = {'osh':15000,'kabob':5000,'tabaka':14000,'free':18000,'chuchvara':20000,'baliq':17000,'qozon kabob':22000,'mastava':1300}
# buyurtma =[]
# for n in range(0,3):
#     buyurtma.append(input(f"{n+1}-chi taomni kiriting : "))
# for taom in buyurtma:
#     if taom in taomlar_royxati:
#         print(f"{taom.title()} {taomlar_royxati.get(taom)} so'm") 
#     else:
#         print(f"\nKechirasiz, bizda {taom.lower()}  yo'q")
 
