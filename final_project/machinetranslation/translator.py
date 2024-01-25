from deep_translator import MyMemoryTranslator

def english_to_urdu(english_text):
    """
    Translate English text to Urdu

    Args:
        english_text (str): Text to be translated to Urdu

    Returns:
        str: Translated text in Urdu
    """
    translator = MyMemoryTranslator(source='en-US', target='ur')  # Use 'ur' for Urdu
    urdu_text = translator.translate(text=english_text)
    return urdu_text


def urdu_to_english(urdu_text):
    """
    Translate Urdu text to English

    Args:
        urdu_text (str): Text to be translated to English

    Returns:
        str: Translated text in English
    """
    translator = MyMemoryTranslator(source='ur', target='en-US')  # Use 'ur' for Urdu
    english_text = translator.translate(text=urdu_text)
    return english_text
