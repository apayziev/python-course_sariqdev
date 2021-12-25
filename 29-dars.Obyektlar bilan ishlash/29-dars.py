# -*- coding: utf-8 -*-
"""
29-DARS. OBYKETLAR BILAN ISHLASH

"""

"""AMALIYOT"""

#1]

# class Avto:
#     """Automobiles"""
#     def __init__(self, brand, model, color, price, year):
#         """Car properties"""
#         self.car_brand = brand
#         self.car_model = model
#         self.car_color = color
#         self.car_price = price
#         self.car_year = year
#         self.car_km = 0
#         self.car_engine = ""
    
#     def get_brand(self):
#         return self.car_brand
#     def get_model(self):
#         return self.car_model
#     def get_color(self):
#         return self.car_color
#     def get_price(self):
#         return self.car_price
#     def get_year(self):
#         return self.car_year
    
#     def set_km(self, km):
#         self.car_km = km
    
#     def set_engine(self, engine):
#          self.car_engine = engine
    
#     def get_info(self):
#         return "Brand: {}, Model: {}, Color: {}".format(first_car.car_brand, first_car.car_model, first_car.car_color)
# first_car = Avto("BMW", "X5", "black", "$50000","2021")
# first_car.set_km(10)
# print(first_car.get_info())
        
#2]

class CarShop:
    """THis is car shop"""
    
    def __init__(self,name, address):
        self.name = name
        self.address = address
        self.availabe_cars = ["BMW","Audi","Gentra","Taxoe"]
        
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def add_newcar(self, new_car):
         self.availabe_cars.append(new_car)
    def get_availableCars(self):
        return user_input.availabe_cars
  
    def get_info(self):
        return f"Car shop name : {user_input.get_name()}, Address : {user_input.get_address()}, Available cars list: {user_input.get_availableCars()} "
    
user_input = CarShop("Python","pystreet 15A")
print(user_input.get_info())


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    