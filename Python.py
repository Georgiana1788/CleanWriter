import spacy
from spacy.matcher import Matcher

def load_model(lang):
    if lang == "ro":
        return spacy.load("ro_core_news_sm")
    elif lang == "en":
        return spacy.load("en_core_web_sm")
    elif lang == "it":
        return spacy.load("it_core_news_sm")
    elif lang == "de":
        return spacy.load("de_core_news_sm")

def simple_filter(text, nlp):
    matcher = Matcher(nlp.vocab)
    bad_words = ["vulgar", "vulgare", "vulgäre", "nepotrivite", "inappropriate", "unangemessene"]
    for word in bad_words:
        matcher.add(word, [[{"LOWER": word}]])
    doc = nlp(text)
    spans = [doc[start:end] for _, start, end in matcher(doc)]
    clean_text = text
    for span in spans:
        clean_text = clean_text.replace(span.text, "[...]")
    return clean_text

test_texts = {
    "ro": "Acesta este doar un text simplu de test, să vedem dacă CleanWriter elimină cuvintele vulgare sau nepotrivite.",
    "en": "This is just a simple test text to check if CleanWriter filters out any vulgar or inappropriate words.",
    "it": "Questo è solo un semplice testo di prova per verificare se CleanWriter rimuove parole volgari o inappropriate.",
    "de": "Dies ist nur ein einfacher Testtext, um zu prüfen, ob CleanWriter vulgäre oder unangemessene Wörter entfernt."
}

for lang, text in test_texts.items():
    print(f"\n=== Language: {lang.upper()} ===")
    nlp = load_model(lang)
    cleaned = simple_filter(text, nlp)
    print(f"Original: {text}")
    print(f"Cleaned:  {cleaned}")