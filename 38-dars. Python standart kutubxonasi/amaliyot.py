# -*- coding: utf-8 -*-
"""
38-DARS. PYTHON STANDART KUTUBXONASI

"""

"""AMALIYOT"""

#1]

# import datetime as dt
# import re

# for i in range(15, 27):
#     sana = dt.date(2022, 1, i)
#     print(sana)

#2]

# def how_many_days_passed_since_youborn():
#     right_now = dt.datetime.today()
#     user_birthyear = int(input("Birthyear: (2000) : "))
#     user_birthmonth = int(input("Birthmonth (1) : "))
#     user_birthdate = int(input("Birthdate (12) : "))
#     whole_birth = dt.date(user_birthyear, user_birthmonth, user_birthdate)
#     return f"{right_now.year - user_birthyear} years, {12*(right_now.year - user_birthyear)} months,{(right_now.date()- whole_birth).days} days "
# print(how_many_days_passed_since_youborn())

#3]

# import re

# template = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# number = input("Enter your phone number : ")
# result = re.match(template, number)
# print(result)

#4]


# with open("sample_text.txt", 'r+') as txt_file:
#     text = txt_file.read()

# result = re.findall(r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*))', text)

# print(result)


