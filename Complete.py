import spacy
from spacy.matcher import PhraseMatcher

def load_language_model(lang_code="ro"):
    try:
        if lang_code == "ro":
            return spacy.load("ro_core_news_sm")
        elif lang_code == "en":
            return spacy.load("en_core_web_sm")
        elif lang_code == "de":
            return spacy.load("de_core_news_sm")
        elif lang_code == "it":
            return spacy.load("it_core_news_sm")
        else:
            print(f"⚠️ Limbaj necunoscut: {lang_code}, folosesc română implicit.")
            return spacy.load("ro_core_news_sm")
    except Exception as e:
        print(f"❌ Eroare la încărcarea modelului SpaCy: {e}")
        return None

def detect_inappropriate(text, lang_code="ro"):
    nlp = load_language_model(lang_code)
    if not nlp:
        return []

    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    
    # Exprimări indecente (pot fi personalizate / extinse)
    patterns = [
        "fă sex", "dă-i la muie", "suge pula", "mănâncă cur",
        "fuck you", "suck dick", "blow job", "eat ass",
        "arsch lecken", "blase ihn", "leck mich",
        "pompino", "fai sesso", "lecca il culo"
    ]
    patterns = [nlp.make_doc(pat) for pat in patterns]
    matcher.add("INAPPROPRIATE", patterns)

    doc = nlp(text)
    matches = matcher(doc)

    flagged_phrases = [doc[start:end].text for match_id, start, end in matches]
    return flagged_phrases

def main():
    print("🌱 CleanWriter CLI - Filtru moral text")
    print("✅ Limbaj implicit: română. Scrie 'exit' pentru a ieși.")
    while True:
        text_input = input("\nScrie textul tău aici: ").strip()
        if text_input.lower() == "exit":
            print("👋 La revedere!")
            break
        lang = input("Limbă (ro/en/de/it): ").strip().lower()
        if not lang:
            lang = "ro"
        found = detect_inappropriate(text_input, lang)
        if found:
            print(f"❌ Textul conține cuvinte nepotrivite: {found}")
        else:
            print("✅ Textul este curat și decent.")

if __name__ == "__main__":
    main()