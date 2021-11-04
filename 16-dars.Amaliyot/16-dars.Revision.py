# -*- coding: utf-8 -*-
"""
16-DARS. REVISION
"""

#1]
# first_author = {'surname':'Navoiy',
#                 'name':'Alisher',
#                 'birth':1441,
#                 'birth_place':'hirat',
#                 'job':'writer'}
# second_author= {'surname':'Ulug\'bek',
#                 'name':'Mirzo',
#                 'birth':1394,
#                 'birth_place':'Samarqand',
#                 'job':'math scientist'}
# third_author = {'surname':'Al-Xorazmiy',
#                 'name':'Muso',
#                 'birth':783,
#                 'birth_place':'Xorazm',
#                 'job':'creator of algebra'
#                 }
# all_authors = [first_author, second_author, third_author]
# for all_a in all_authors:
#     print(f"{all_a['name']} {all_a['surname']} was born in {all_a['birth_place'].title()} , in {all_a['birth']}. His is famous {all_a['job']}.")

#2]

# first_author['books'] = ['Hayrat ul Abror','Xamsa']
# second_author['books'] = ['Zijji jadiy ko\'ragoniy','Yulduzlar haqida']
# third_author['books'] =['Algebra haqida','Algebraga kirish']
# for all_a in all_authors:
#     print(f"\n{all_a['name']} {all_a['surname']}\'s books are ")
#     book = all_a.get('books')
#     for n in book:
#         print(f"{n}")
        
#3]
# friends_movies = {'bexruz':['Squid Game','Terminator','Godzilla vs KingKong'],
#                   'jaloliddin':['Chuqur','Ichkarida','Sevgi iztirobi'],
#                   'nizomiddin':['Suv va olov','Uch savdoyi','Five feet apart']}
# for name,movies in friends_movies.items():
#     print(f"\n{name.title()}'s favourite movies :  ")
#     for movie in sorted(movies):
#         print(movie)

#4]

countries = {"O'zbekiston":
              {'poytaxti':'Toshkent','hududi':'489.9km',"pul birligi":" so'm"},
              'Rossiya':
                  {'poytaxti':"Moskva",'hududi':'1000.9km',"pul birligi":" rubl"},
              'Turkiya':
                  {'poytaxti':'Istambul','hududi':'800.9km',"pul birligi":"lira"},
              'Qozog\'iston':
                  {'poytaxti':'Astana','hududi':'900.9km',"pul birligi":"tenge"},
              'Fransiya':
                  {'poytaxti':'Parij','hududi':'700.9km',"pul birligi":"dollar"},
              'Buyuk Britanya':{'poytaxti':'London','hududi':'875.9km',"pul birligi":"dollar"}
              }
# print('Information about countries :\n ')

# for country_name, country_info in sorted(countries.items()):
#     print(f"\n{country_name}\'s capital is {country_info['poytaxti']}",
#           f"\nTerritory : {country_info['hududi']}",
#           f"\nCurrency : {country_info['pul birligi']}"
#           )

#5]
user_input = input("Enter the country name : ").title()
if user_input in countries:
    info = countries[user_input]
    print(f"\n{user_input}\'s capital is {info['poytaxti']}",
          f"\nTerritory : {info['hududi']}",
          f"\nCurrency : {info['pul birligi']}")
else:
    print(f"There is no {user_input} in our base ")







