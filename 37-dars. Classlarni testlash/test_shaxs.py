from shaxs import Shaxs, Talaba
 
import unittest

class ShaxsTest(unittest.TestCase):
    """Test shaxs class"""
    def setUp(self):
       
        self.shaxs1 = Shaxs("Eshmat", "Eshmatov", "AB8742777", 2000)
    
    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)   
        
    def test_get_age(self):
        self.assertEqual(self.shaxs1.get_age(2022), 22)
        
    def test_get_info(self):
        self.assertAlmostEqual(self.shaxs1.get_info(), "Eshmat Eshmatov. Passport:AB8742777, 2000-yilda tug`ilgan")

if __name__ == '__main__':
    unittest.main()

    
    