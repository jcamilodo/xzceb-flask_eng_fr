"""System module."""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This code acts as a translator from English to French
    """
    memory_translator = MyMemoryTranslator(source = "en-US", target = "fr-FR")
    french_text = memory_translator.translate(text = english_text)
    return french_text

def french_to_english(french_text):
    """
    This code acts as a translator from French to English
    """
    memory_translator = MyMemoryTranslator(source = "fr-FR", target = "en-US")
    english_text = memory_translator.translate(text = french_text)
    return english_text
