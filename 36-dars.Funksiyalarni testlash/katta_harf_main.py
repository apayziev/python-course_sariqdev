from matn_1harf import kattaHarf, matn_2

import unittest

class KattaHarf(unittest.TestCase):
    def test_katta_harfmi(self):
        self.assertTrue(kattaHarf(),matn_2())

if __name__ == '__main__':
    unittest.main()

    