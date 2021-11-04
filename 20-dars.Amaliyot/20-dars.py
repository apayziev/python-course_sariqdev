"""
20-DARS. QIYMAT QAYTARUVCHI FUNKSIYA
"""

"""AMALIYOT"""

#1]
# def user_info(ism, familiya, yosh, tyil, tjoy, email, tel):
#     user_info_dic = {'ism':ism,
#                      'familiya':familiya,
#                      'yosh':yosh,
#                      'tyil':tyil,
#                      'tjoy':tjoy,
#                      'email':email,
#                      'tel':tel
#                      }
#     return user_info_dic
# storages = []
# while True:
#     ism = input("Ism : ")
#     familiya = input('Familiya : ')
#     yosh = int(input('Yoshingiz: '))
#     tyil = int(input('Tug\'ilgan yilingiz: '))
#     tjoy = input('Tug\'ilgan joyingiz : ')
#     email = input('Emailingiz : ')
#     tel = input('telefon raqamingiz :')
#     ask = input("Yana ma'lumot kiritishni hohlaysizmi (yes/no) : ")
#     storages.append(user_info(ism, familiya, yosh, tyil, tjoy, email, tel))
    
#     if ask !='yes':
#         break

# for storage in storages:
#     print(f"{storage['ism'].title()} {storage['familiya'].title()}"
#           f"{storage['tyil']} yilda tug'ilgan,hozirda {storage['tjoy']}da istiqomat qiladi.\n",
#           f"Hozirda {storage['yosh']} yoshda.\nUning emaili : {storage['email']}")


#2]
#1-way:
# def kattasiniTop(num1, num2, num3):
#     while True:
#         number = num1
#         if number > num2 and number > num3:
#             print(f"{number} eng kattasi")
#         elif num2 > number and num2 > num3:
#             print(f"{num2} eng katta son")
#         else:
#             print(f"{num3} eng kattas son")
#         break
        
# num1 = int(input('Num1 : '))
# num2 = int(input('Num2 : '))
# num3 = int(input('Num3 : '))
# print(kattasiniTop(num1, num2, num3))

#2-way:
    
# def kattasi(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max
# print(kattasi(10,20,0))

        
    

    