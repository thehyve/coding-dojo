import unittest
from diamond import diamond

class DiamondTestCase(unittest.TestCase):

    def test_A_diamond(self):
        self.assertEqual(diamond('A'), 'A')

    def test_B_diamond(self):
        self.assertEqual(diamond('B'), 
        ' A \nB B\n A ')

    def test_C_diamond(self):
        self.assertEqual(diamond('C'), 
        '  A  \n B B \nC   C\n B B \n  A  ')

if __name__ == '__main__':
    unittest.main()
