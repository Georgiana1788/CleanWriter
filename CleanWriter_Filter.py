import spacy

# Încarcă modelele NLP pentru limbile suportate
nlp_models = {
    "ro": spacy.blank("ro"),  # dacă există model disponibil, încarcă-l
    "en": spacy.load("en_core_web_sm"),
    "de": spacy.load("de_core_news_sm"),
    "it": spacy.load("it_core_news_sm")
}

# Listă simplă de cuvinte indecente pe care să le filtreze strict
BAD_WORDS = ["fuck", "shit", "pizda", "curva", "cazzo", "scheiß", "merda", "fick"]

def clean_text(text, lang="en"):
    nlp = nlp_models.get(lang, nlp_models["en"])
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.text.lower() not in BAD_WORDS:
            filtered_tokens.append(token.text)
        else:
            filtered_tokens.append("***")
    return " ".join(filtered_tokens)