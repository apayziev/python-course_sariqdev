from juft_sonlar import juft_sonlar as js

import unittest

class JuftSonlar(unittest.TestCase):
    def test_juft_sonlarmi(self):
        self.assertAlmostEqual(js(), [i for i in range(0,21) if i % 2 == 0])

if __name__ == '__main__':
    unittest.main()
