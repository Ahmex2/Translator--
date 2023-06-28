from deep_translator import MyMemoryTranslator

# Initialize the translator with English as the source language and French as the target language
global_translator = MyMemoryTranslator(source='en', target='fr')

def translate_english_to_french(text):
    """
    Translates English text to French using the MyMemoryTranslator API.
    """
    try:
        translation = global_translator.translate(text)
    except Exception as e:
        # Handle errors and exceptions gracefully
        print(f"Error: {e}")
        return "Translation not available"
    return translation

def translate_french_to_english(text):
    """
    Translates French text to English using the MyMemoryTranslator API.
    """
    local_translator = MyMemoryTranslator(source='fr', target='en')
    try:
        translation = local_translator.translate(text)
    except Exception as e:
        # Handle errors and exceptions gracefully
        print(f"Error: {e}")
        return "Translation not available"
    return translation