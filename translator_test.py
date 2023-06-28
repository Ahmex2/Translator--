import unittest
from translator import translate_english_to_french, translate_french_to_english

class TestTranslator(unittest.TestCase):
    def test_french_to_english_equal(self):
        self.assertEqual(translate_french_to_english('Bonjour'), 'Hello')
        
    def test_french_to_english_not_equal(self):
        self.assertNotEqual(translate_french_to_english('Bonjour'), 'Bonsoir')
        
    def test_english_to_french_equal(self):
        self.assertEqual(translate_english_to_french('Hello'), 'Bonjour')
        
    def test_english_to_french_not_equal(self):
        self.assertNotEqual(translate_english_to_french('Hello'), 'Bonjour tout le monde')
        
def translate_english_to_french(word):
    """
    Translates a word from English to French.
    """
    translations = {
        'Hello': 'Bonjour',
        'Goodbye': 'Au revoir',
        'Thank you': 'Merci',
        'Yes': 'Oui',
        'No': 'Non'
    }
    return translations.get(word, None)
if __name__ == '__main__':
    unittest.main()