"""17-DARS. WHILE TSIKL OPERATORI"""

"""
AMALIYOT
"""

#1]

#1-way: break yordamida bajarish
# kitoblar = []
# while True:
#     kitob = input('Sevimli kitobingizni nomini kiriting : ')
#     kitoblar.append(kitob)
#     if kitoblar[-1] == 'stop':
#         del kitoblar[-1]
#     if kitob == 'stop':
#         break
# print("\nSizning sevimli kitoblaringiz ro\'yxati: ")
# for n in kitoblar:
#     print(n)

# 2-way : ishorani o'zgartirish yordamida
# value = True
# while value:
#     user_input = input('Sevimli kitobingizni kiriting : ')
#     if user_input == 'stop':
#         value = False
#     else:
#         print(value)

# 3-way : shart tekshirish yordamida
# qiymat = ' '
# while qiymat != 'stop':
#     qiymat = input('Sevimli kitobingizni kiriting :')
#     if qiymat != 'stop':
#         print(qiymat)
# print('dastur tugadi')

#2]

#1-way:

    # while True:
#     qiymat = input("Yoshingizni kiriting: ")
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
        
#     if yosh < 7:
#             narh = 2000
#     elif yosh <= 18:
#             narh = 8000
#     elif yosh <= 65:
#             narh = 12000
#     else:
#             narh = 0
            
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")  
   
    
#2-way:      
# user = ''
# while user != 'exit' or user !=' stop':
#     user = str(input('Yoshingizni kiriting : '))
#     if user != 'exit' or user != 'stop':
#         if int(user) < 7:
#             narh = 2000
#         elif int(user) <= 18:
#             narh = 8000
#         elif int(user) <= 65:
#             narh = 12000
#         else:
#             narh = 0
#         print(f"Chipra narxi siz uchun {narh} so'm ")
# print('dastur tugadi')

#3-way:
# value = True
# while value:
#     user = int(input('Yoshingizni kiriting : '))
#     if user_input == 'stop':
#             if user < 7:
#                 narh = 2000
#             elif user <= 18:
#                 narh = 8000
#             elif user <= 65:
#                narh = 12000
#             else:
#                    narh = 0
#     print(f"Chipra narxi siz uchun {narh} so'm ")
#     value = False
  
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
sonlar = {'one':1,'two':2,'three':'3','four':4,'five':5}
result = 0
user_input1 = input('Enter the number : ')
user_input2 = input('Enter the number : ')
for value in sonlar.values():
    result = int(sonlar[user_input1]) + int(sonlar[user_input2])
print(result)






