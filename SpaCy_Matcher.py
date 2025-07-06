import spacy
from spacy.matcher import PhraseMatcher

def load_language_model(lang_code="ro"):
    if lang_code == "ro":
        return spacy.load("ro_core_news_sm")
    elif lang_code == "en":
        return spacy.load("en_core_web_sm")
    elif lang_code == "de":
        return spacy.load("de_core_news_sm")
    elif lang_code == "it":
        return spacy.load("it_core_news_sm")
    else:
        raise ValueError("Unsupported language code.")

def detect_inappropriate(text, lang_code="ro"):
    nlp = load_language_model(lang_code)
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

    # pattern-uri simple
    patterns = [
        "dă-i la muie", "fă sex", "suge pula", "mănâncă cur",
        "fuck you", "suck dick", "give head",
        "arsch lecken", "blase ihn",
        "pompino", "fai sesso"
    ]
    patterns = [nlp.make_doc(pat) for pat in patterns]
    matcher.add("INAPPROPRIATE", patterns)

    doc = nlp(text)
    matches = matcher(doc)

    flagged_phrases = []
    for match_id, start, end in matches:
        span = doc[start:end]
        flagged_phrases.append(span.text)

    return flagged_phrases

# CLI usage
if __name__ == "__main__":
    text_input = input("Scrie textul tău aici: ")
    lang = input("Limbă (ro/en/de/it): ").lower()
    found = detect_inappropriate(text_input, lang)
    if found:
        print("❌ Textul conține sugestii / cuvinte nepotrivite:", found)
    else:
        print("✅ Textul pare curat.")