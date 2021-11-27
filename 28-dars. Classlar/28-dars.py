
"""
28-DARS. KLASSLAR

"""

"""AMALIYOT"""
#1]

class User:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,name,surname,username, email, tel):
        """Talabaning xususiyatlari"""
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.tel = tel
        
    def full_name(self):
        return f"{self.name} {self.surname}"
    
    def get_email(self):
        return 
        
 
    def describe(self):
        print("Information about sample user : \n"
            f"Username : {self.username}, Ismi : {user_info.full_name()}, email: {self.email}, tel number: {self.tel}\n"
            f"-------------------------------------------------------------------------")

user_info = User('Azimjon', 'Pulatov', 'azimjondev', 'azimjon@mailcom', +99899777777)
user_info.describe()

user_info2 = User('Mamarayim', 'Eshmatov', 'mamarayimdev', 'mamarayimjon@mailcom', +998997177777)
user_info2.describe()

user_info3= User('Eshmat', 'Mamarayimov', 'eshmatdev', 'eshmatdev@mailcom', +998997077777)
user_info3.describe()