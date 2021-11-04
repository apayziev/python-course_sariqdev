# -*- coding: utf-8 -*-
"""
18-DARS. WHILE TSIKLINING RO'YXATLAR VA LUG'ATLARDA ISHLATILISHI
"""

"""
AMALIYOT QISMI:
"""
#1]
#1-way:
    
# user_order = []
# n = 1
# while True:
#     user_input = input(f"{n} - chi taomni kiriting : ")
#     user_order.append(user_input)
#     n += 1
#     if user_input == 'yo\'q':
#         break

# del user_order[-1]        
# print("Siz kiritgan taomlar ro'yxati : ")
# for order in user_order:
#     print(order)    

#2-way:
    
# buyurtmalar = []
# tartib = 1
# sign = True
# savol = 'Yana buyurtma qilishni hohlaysizmi (ha / yo\'q) : '
# while sign:
#     user_input = input(f"{tartib} - chi taomni kiriting : ")
#     buyurtmalar.append(user_input)
#     javob = input(savol).lower()
    
#     if javob == 'ha':
#         tartib += 1
#     else: 
#         sign = False

# print("\nSiz kiritgan taomlar ro'yxati 📃: ")
# for buyurtma in buyurtmalar:
#     print(f"✔️ {buyurtma}")
# print('\nYuqoridagi buyurtmalar qabul qilindi 👌')

#3-way:
    
# buyurtmalar_list = []
# tartib = 1
# savol_davomi = 'Yana buyurtma qilishni hohlaysizmi (yes / no) : '
# user_input = ''
# while user_input != 'no':
#     user_input = input(f"{tartib} - chi taomni kiriting : ").lower()
#     buyurtmalar_list.append(user_input)
#     javob = input(savol_davomi)
#     if javob != 'no':
#         tartib += 1
#     else:
#         break
# print("\nSiz kiritgan taomlar ro'yxati 📃: ")
# for buyurtma in sorted(buyurtmalar_list):
#     print(f"✔️ {buyurtma}")
# print('\nYuqoridagi buyurtmalar qabul qilindi 👌')


#2]
# mahsulotlar = {} 
# while True: 
#     mahsulot = input("Mahsulot nomini kiriting: ") 
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ") 
#     mahsulotlar[mahsulot] = narh 
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q) ") 
#     if javob != 'ha': 
#         break
    
# print("Siz kiritgan mahsulotlar va ularning narxlari: \n")
# for mahsulott,value in mahsulotlar.items():
#     print(f"{mahsulott}:",
#           f"{value} so'm\n")

#3]
#1-way:
    
# orders = ['anor','gilos','olma','qovun','anjir','behi','banan','kivi','xurmo']
# eBozor = {'anor':7000,'olma':6500,'gilos':40000,'anjir':8000,'behi':10000,
#           'qovun':25000,'tarvuz':20000,'qulupnay':30000,'nok':12000}
# while True:
#     for order in sorted(orders):
#         if order in eBozor:
#             print(f"{order.title()} - {eBozor[order]} so'm")
#         else:
#             print(f"Bizda {order} yo'q ")
#     break

#2-way:
    
# orders = ['anor','gilos','olma','qovun','anjir','behi','banan','kivi','xurmo']
# eBozor = {'anor':7000,'olma':6500,'gilos':40000,'anjir':8000,'behi':10000,
#           'qovun':25000,'tarvuz':20000,'qulupnay':30000,'nok':12000}

# while orders:
#     buyurtma = orders.pop()
#     if buyurtma in eBozor.keys():
#         narh = eBozor[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")
