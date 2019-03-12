import unittest
from code_cracker import decrypt, encrypt

class CodeCrackerTestCase(unittest.TestCase):
    
    def test_alphabet_translation(self):
        decrypted_msg = decrypt('! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o')
        self.assertEqual(decrypted_msg, 'a b c d e f g h i j k l m n o p q r s t u v w x y z')

    def test_reverse_alphabet_translation(self):
        decrypted_msg = decrypt('! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o'[::-1])
        self.assertEqual(decrypted_msg, 'a b c d e f g h i j k l m n o p q r s t u v w x y z'[::-1])

    def test_alphabet_retranslation(self):
        encrypted_msg = encrypt('a b c d e f g h i j k l m n o p q r s t u v w x y z')
        self.assertEqual(encrypted_msg, '! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o')

if __name__ == '__main__':
    unittest.main()
