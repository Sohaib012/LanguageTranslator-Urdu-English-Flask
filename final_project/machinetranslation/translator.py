"""
Module to translate text between English and French using the deep_translator's MyMemoryTranslator
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French

    Args:
    english_text (str): Text to be translated to French

    Returns:
    str: Translated text in French
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = translator.translate(text=english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English

    Args:
    french_text (str): Text to be translated to English

    Returns:
    str: Translated text in English
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    english_text = translator.translate(text=french_text)
    return english_text
