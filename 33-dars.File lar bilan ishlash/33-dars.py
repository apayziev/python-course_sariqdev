# -*- coding: utf-8 -*-
"""
#33 FAYLLAR BILAN ISHLASH 
"""
import pickle

# with open('pi.txt') as file:
#     pi = file.read()
# # print(pi)
# pi = pi.rstrip()
# pi = pi.replace("\n","")
# print(type(float(pi)))

# with open('txt.txt') as file:
#     words = [word.replace("\n", '') for word in file.readlines()]
# print(words)

# with open('lesson.txt',"w+") as file:
#     file.write("Welcom to 33rd lesson")

# with open('lesson.txt',"a+") as file:
#     file.write("\t"+"Thanks")

# variable1 = {"Name":"Hasan","Surname":"Husanov","tyil":"2003","kurs":2}
# variable2 = ['Hasan',"Husan","Mamarayim","Eshmat"]

# with open('newpickelfile',"wb") as file:
#     pickle.dump(variable1, file)
#     pickle.dump(variable2, file)
    
# with open('newpickelfile',"rb") as file:
#     print(pickle.load(file))
    
#Amaliyot

#2]
# with open("What I learned.txt") as file:
#     print(file.read())

#3]
# with open("pi_million_digits.txt","r+") as file:
#     filename = file.read().rsplit()
#     print("02012002" in str(filename).replace("\n",""))

#3]

# with open("pi_million_digits.txt") as file:
#     pi = file.read()
#     pi = pi.rstrip()
#     pi = pi.replace("\n","")
#     PI = float(pi)
    
# with open("pi_million_digits.txt","wb") as picklefile:
#     pickle.dump(PI,picklefile)

#4]

while True:
    print("Dasturdan chiqish uchun 'Enter' ni bosing")
    user_input = input("Matn kiriting men text file ochib saqlab boraman: ")
    if user_input == "":
        print("Dastur yakunlandi!")
        break
    with open('new_txt_file.txt',"a") as file:
            file.write(user_input + "\n")