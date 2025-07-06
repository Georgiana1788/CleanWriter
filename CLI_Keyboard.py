# cli_keyboard.py
# Un mic corector moral pentru text, suport RO/EN/DE/IT

from langdetect import detect
import json

# ------------- Configurare filtrare cuvinte -------------
FILTERS = {
    "ro": {
        "sensibile": ["muie", "pula", "cur", "dracu", "rahat"],
        "alternative": ["(limbaj decent)"]
    },
    "en": {
        "sensibile": ["fuck", "shit", "bitch", "ass", "whore", "handicapated"],
        "alternative": ["(be polite)"]
    },
    "de": {
        "sensibile": ["scheiße", "fick"],
        "alternative": ["(höflich bleiben)"]
    },
    "it": {
        "sensibile": ["cazzo", "merda"],
        "alternative": ["(usa parole gentili)"]
    }
}

# ---------------------------------------------------------
def clean_text(text, lang_code):
    data = FILTERS.get(lang_code, {})
    sensibile = data.get("sensibile", [])
    cleaned = text

    for word in sensibile:
        if word in cleaned.lower():
            cleaned = cleaned.replace(word, "***")
    
    return cleaned

# ---------------------------------------------------------
# Main CLI loop
if __name__ == "__main__":
    print("Introdu textul tău:")
    text = input("> ")

    lang_code = detect(text)
    print(f"\n📌 Limbă detectată: {lang_code.upper()}")

    cleaned_text = clean_text(text, lang_code)
    print(f"\n✅ Text curățat:\n{cleaned_text}")