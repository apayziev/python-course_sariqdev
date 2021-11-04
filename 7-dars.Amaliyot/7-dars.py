#07-DARS. LIST (RO'YXAT)

#AMALIYOT

#1)ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

# ismlar = ["Dilshod" , "Bexruz" , "Shahzod", "Nizomiddin"]
# print(ismlar)

# #2)Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
    
# print("Salom " + ismlar[0] + ", bugun choyxona bormi?")
# print(ismlar[1] + ", choyxonaga boramizmi?")

#3)Sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun ,o'nlik).

sonlar = [10,-5,10.5]
# print(sonlar)

#4) Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.

print(sonlar[1]+sonlar[2])
sonlar.append(13)
print(sonlar)
del sonlar[3]
print(sonlar)
sonlar.insert(0,15)
print(sonlar)

#5)
t_shaxslar = ["Amir Temur", "Ibn Sino","Beruniy"]
x_shaxslar = ["Bill Gates", "Stive Jobs"]
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, \nzamonaviy shaxslardan esa {x_shaxslar.pop(0)} bilan \nsuhbat qilishni istar edim\n")

#6)

# friends = []
# friends.append('Dilshod')
# friends.append('Mamatqul')
# friends.append('Eshmat')
# friends.insert(-1,'Toshmat')
# print(friends)
# friends.insert(0,"G'ishmat")
# print(friends)
# del friends[1]
# print(friends)
# friends.remove('Eshmat')
# print(friends)
# del friends[-1]
# print(friends)

#7)
friends = ["G'ishmat", "Toshmat", "Mamarayim", "Eshmat", "Rais buva"]
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar : ", mehmonlar)
