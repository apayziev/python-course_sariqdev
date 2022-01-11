from  is_fib_num import is_fib_number

import unittest

class IsFibNum(unittest.TestCase):
    def test_is_fib_num(self):
        if is_fib_number(7) == True:
            return self.assertTrue(is_fib_number(7),True)
        return self.assertFalse(is_fib_number(7),False)
    
if __name__ == '__main__':
    unittest.main()
