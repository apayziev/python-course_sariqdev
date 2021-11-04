# -*- coding: utf-8 -*-
"""
15 - DARS. LUG'AT ELEMENTLARI BILAN ISHLASH
"""

""" AMALIYOT """

#1)

# python_dictionary = {'integer':'butun son qaytaradi','double':"o'nlik son qayataradi",
#                      'sort()':'saralab beradi', 'sorted()':'bir marotaba saralab beradi',
#                      'boolean':'mantiqiy qiymat','if':'shartlarni tekshiradi'}

# for key,value in sorted(python_dictionary.items()):
#     print(f"{key.title()} - {value}"\n)

#2)

davlatlar = {'O\'zbekiston':'Toshkent', 'Rossiya':'Moskva','Turkiya':'Istambul',
              'Qozog\'iston':'Astana', 'Fransiya':'Parij','Buyuk Britanya':'London'}
print("Dunyo davlatlari : ")
for key in sorted(davlatlar.keys()):
    print(f"{key.upper()}")
for davlat in sorted(davlatlar):
    print(f"{davlat.upper()}")
print("\nPoytaxtlari : ")
for value in sorted(davlatlar.values()):
    print(value)

#3)
#1-way
# davlatlar = {'O\'zbekiston':'Toshkent', 'Rossiya':'Moskva','Turkiya':'Istambul',
#               'Qozog\'iston':'Astana', 'Fransiya':'Parij','Buyuk Britanya':'London'}
# user_input = str(input('Davlat nomini kiriting : '))
# capital = davlatlar.get(user_input.title())
# # print(f"{user_input} - {capital}")
# if capital == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{user_input.title()} - {capital}")

#2-way

# davlatlar = {'O\'zbekiston':'Toshkent', 'Rossiya':'Moskva','Turkiya':'Istambul',
#               'Qozog\'iston':'Astana', 'Fransiya':'Parij','Buyuk Britanya':'London'}
# user_input = str(input('Davlat nomini kiriting : '))
# capital = davlatlar.get(user_input.title(),'Ro\'yxatda bunday davlat mavjud emas ')
# print(f"{user_input.title()} - {capital}")

#4)

# menu = {'Osh':'15000', 'Manti':'5000','Norin':'20000','Free':'18000','Lag\'mon':'1200',
#         'Chuchvara':'16000','Tabaka':'14000'}
# print("Assalomu alekum, buyurtma bermochi bo'lgan taomlaringizni kiriting : ")

# ordered=[]
# for n in range(3):
#     ordered.append(input(f"{n+1} chi taom : ").title())
# print(f"Sizning buyurtmalaringiz:\n{ordered}")

# for order in ordered:
#     if order in menu:
#         print(f"{order.title()} {menu[order]} so'm") # {menu.get(order)}
#     else:
#         print(f"Kechirasiz, bizda {order.lower()}  yo'q")

