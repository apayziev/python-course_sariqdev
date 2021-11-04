# -*- coding: utf-8 -*-
"""
16-DARS. NESTING
"""
"""AMALIYOT"""

#1)
# first_person = {'surname':'jobs',
#                 'name':'stive',
#                 'birth':'1977',
#                 'birth_place':'Syria',
#                 'job':'project manager',
#                 'company':['Apple','Microsoft']}
# second_person = {'surname':'gates',
#                  'name':'bill',
#                  'birth':'1967',
#                  'birth_place':'USA',
#                  'job':'programmer',
#                  'company':['Microsoft','Google']}
# third_person = {'surname':'newport',
#                 'name':'call',
#                 'birth':'1977',
#                 'birth_place':'UK',
#                 'job':'lecturer',
#                 'company':['Airnbn','Google']}
# all_person =[first_person,second_person,third_person]
# for all_p in all_person:
#     print(f"{all_p['name'].title() }"
#           f" {all_p['surname'].title()} was born in "
#           f"{all_p['birth']}, "
#           f"{all_p['birth_place']}."
#           f" He worked as a {all_p['job']}.👌")

#2]
# for all_p in all_person:
#     companies = all_p.get('company')
#     print(f"\n{all_p['name'].title()} is a CEO of ")
#     for company in companies:
#         print(company)
         
#3]
# ism_kinolarRoyxati={'Dilshod':['shaytanat','bo\'rilar','panoh'],
#                     'Behruz':['Forsaj','venom','godizlla'],
#                     'Nizomiddin':['American.Sniper','Five.Feet.Apart','Soul']}
# for ism, kinolar in ism_kinolarRoyxati.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)
        
#4]

# davlatlar = {"O'zbekiston":
#               {'poytaxti':'Toshkent','hududi':'489.9km',"pul birligi":" so'm"},
#               'Rossiya':
#                   {'paytaxti':"Moskva",'hududi':'1000.9km',"pul birligi":" rubl"},
#               'Turkiya':
#                   {'poytaxti':'Istambul','hududi':'800.9km',"pul birligi":"lira"},
#               'Qozog\'iston':
#                   {'poytaxti':'Astana','hududi':'900.9km',"pul birligi":"tenge"},
#               'Fransiya':
#                   {'poytaxti':'Parij','hududi':'700.9km',"pul birligi":"dollar"},
#               'Buyuk Britanya':{'poytaxti':'London','hududi':'875.9km',"pul birligi":"dollar"}
#               }
# print('Davlatlar haqida ma\'lumot :\n ')
# for davlat, poytaxt in davlatlar.items():
#     print(f"{davlat}: ")
#     print(f"Poytaxti: {poytaxt.get('poytaxti')}"
#           f"\nHududi: {poytaxt['hududi']}"
#           f"\nPul birligi :{poytaxt['pul birligi']}\n")

#5]

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                    'maydon':448978,
                    'aholi':33_000_000,
                    'pul birligi':"so'm"
                    },
    "rossiya":{'poytaxt':"moskva",
                    'maydon':17_098_246,
                    'aholi':144_000_000,
                    'pul birligi':"rubl"
                    },
    "AQSH":{'poytaxt':"vashington",
                    'maydon':9_631_418,
                    'aholi':327_000_000,
                    'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                    'maydon':329750,
                    'aholi':25_000_000,
                    'pul birligi':"rinngit"}
         }

user_input = input('Davlat nomini kiriting: ').lower()
if user_input in davlatlar:
    info = davlatlar[user_input]
    print(f"\n{user_input.capitalize()}ning poytaxti: {info.get('poytaxt').title()}"
          f"\nHududi: {info.get('maydonrossiya')} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")