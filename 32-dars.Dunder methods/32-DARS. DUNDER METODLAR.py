# -*- coding: utf-8 -*-
"""
32-DARS. DUNDER METODLAR
"""

# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
    
#     def __repr__(self):
#         """Obyekt haqida ma'lumot"""
#         return f"Avto: {self.rang} {self.make} {self.model}"


# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.avtolar} avtosaloni"
    
#     def add_avto(self,avto):
#         if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto obyketini kiriting")
    
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self,index):
#        return self.avtolar[index]

# salon1 = AvtoSalon("MaxAvto")
# # Avto obyektlarini yaratamiz
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)

# # Yuqoridagi obyektlarni salon1 ga qo'shamiz
# for avto in [avto1, avto2, avto3]: 
#     salon1.add_avto(avto)

# print(len(salon1))


#Amaliyot

from uuid import uuid4

class Shaxs:
    __odamlar_soni = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni += 1
        
    @classmethod
    def get_odamlar_soni(cls):
        """Umumiy odamlar soni"""
        return cls.__odamlar_soni
    def __repr__(self):
        return self.get_info()
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

inson = Shaxs("Mamarayim","Mamatqulov","XXXXXXXXX",2001)
inson2 = Shaxs("Eshmat","Mamatqulov","XXXXXXXXX",2001)

class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self,ism,familiya,passport,tyil,bosqich = 1):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = uuid4()
        self.__bosqich = bosqich
        Talaba.__talabalar_soni += 1
    
    @classmethod
    def get_talabalar_soni(cls):
        """Umumiy talabar soni"""
        return cls.__talabalar_soni
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.__bosqich
    
    def __lt__(self, talaba2):
        result = self.passport > talaba2.passport
        return result
   
    def __len__(self):
        return len(self.passport)
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.__idraqam}"
        return info

talaba1 = Talaba("Eshmat","Eshmatov","AB777777777777",1999,2)
talaba2 = Talaba("Mamarayim", "Mamatqulov", "AB874277788888888", 2000,2)