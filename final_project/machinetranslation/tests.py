import unittest
from translator import english_to_french, french_to_english

class TestTranslationMethods(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Who are you'), 'تم کون ہو')

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('تم کون ہو'), 'Who are you')

if __name__ == '__main__':
    unittest.main()


