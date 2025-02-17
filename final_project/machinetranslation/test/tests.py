import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour" ) # test equal
    def test2(self): 
        self.assertNotEqual(english_to_french("Hello"), "Bonjourno" ) # test not equal

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hi") # test equal
    def test2(self): 
        self.assertNotEqual(french_to_english("Bonjour"), "Car" ) # test not equal

unittest.main()