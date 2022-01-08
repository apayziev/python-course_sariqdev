# -*- coding: utf-8 -*-
"""
# 30-DARS. VORISLIK VA POLIMORFIZM
"""
"""Amaliyot"""
#1]

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam,talaba_fan):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
        self.yangi_fan = talaba_fan
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
    def fanga_yozil(self):
        result = self.fanlar.append(self.yangi_fan)
        return result
        
class Fan:
    """Fanlar klassi"""
    def __init__(self,fan):
        self.fan = fan
        
    def get_fan(self):
        return self.fan
    
fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Informatika")
talaba = Talaba("Mamarayim", "Mamajonov", "AB8742775", "2021", "N100000", fan3)
print(talaba.fan3.get_fan())