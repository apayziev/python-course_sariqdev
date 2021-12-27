# -*- coding: utf-8 -*-
"""
31-DARS. INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI
"""
""" AMALIYOT """

#1]
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
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
inson = Shaxs("Mamarayim","Mamatqulov","XXXXXXXXX",2001)

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
    def get_talabar_soni(cls):
        """Umumiy talabar soni"""
        return cls.__talabalar_soni
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.__bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.__idraqam}"
        return info
