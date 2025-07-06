import spacy

def load_model(lang):
    models = {
        "ro": "ro_core_news_sm",
        "en": "en_core_web_sm",
        "it": "it_core_news_sm",
        "de": "de_core_news_sm"
    }
    if lang in models:
        try:
            return spacy.load(models[lang])
        except OSError:
            print(f"⚠ Modelul pentru {lang} nu este instalat. Rulează: python -m spacy download {models[lang]}")
            exit(1)
    else:
        print("⚠ Limba aleasă nu este suportată.")
        exit(1)

def simple_filter(text, nlp):
    doc = nlp(text)
    # Exemplu filtrare: scoate cuvinte scurte și punctuația
    cleaned = " ".join([token.text for token in doc if not token.is_punct and len(token.text) > 2])
    return cleaned

if __name__ == "__main__":
    print("=== CleanWriter CLI Interactiv ===")
    lang = input("Alege limba (ro/en/it/de): ").strip()
    nlp = load_model(lang)
    while True:
        text = input("\nScrie textul tău (sau 'exit' pentru ieșire): ").strip()
        if text.lower() == "exit":
            break
        cleaned = simple_filter(text, nlp)
        print("✅ Text filtrat:", cleaned)