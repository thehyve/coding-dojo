import unittest
from code_cracker import decrypt

class CodeCrackerTestCase(unittest.TestCase):
    
    def test_alphabet_translation(self):
        decrypted_msg = decrypt('! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o')
        self.assertEqual(decrypted_msg, 'a b c d e f g h i j k l m n o p q r s t u v w x y z')

if __name__ == '__main__':
    unittest.main()
