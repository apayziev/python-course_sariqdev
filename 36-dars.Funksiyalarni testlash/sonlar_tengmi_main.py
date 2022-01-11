from sonlar_tengmi import sonlar_tengmi
import unittest


class SonlarTengmi(unittest.TestCase):
    def test_sonlar_tengmi(self):
        self.assertEqual(sonlar_tengmi(5, 10,100), 100)

if __name__ == '__main__':
    unittest.main()
