# -*- coding: utf-8 -*-
"""
34- JSON
"""

"""AMALIYOT"""
import json

# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# with open('bemor.json','w') as f:
#     json.dump(bemor,f)
    
#1]

# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data, indent=4)

#2]

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# consolega_chiqarish = "{}\n{}".format(talaba['ism'],talaba['familiya'])
# print(consolega_chiqarish)

#3]

# with open('1-2 task.json', 'w') as json_file:
#     json.dump((data), json_file)
#     json.dump(talaba, json_file)

#4]

# with open("students.json") as file_object:
#     new_list = json.load(file_object)

# for item in new_list['student']:
#     print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")
#5]

with open('api-result.json') as file:
    list_item = json.load(file)
print(list_item["query"]["pages"]["13801"]["title"])
print(list_item["query"]["pages"]["13801"]['extract'])   
result = json.dumps(list_item, indent = 4)
print(result)
