# filters.py

import re

# listă simplă de cuvinte vulgare (poți extinde)
VULGAR_WORDS = {
    "română": ["pula", "cur", "muie", "căcat"],
    "engleză": ["fuck", "shit", "bitch", "asshole"],
    "germană": ["scheiße", "fick", "arschloch"],
    "italiană": ["cazzo", "stronzo", "merda"]
}

def clean_soft(text, language):
    """
    Înlocuiește cuvintele sensibile cu variante estompate (soft).
    """
    for word in VULGAR_WORDS.get(language, []):
        pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
        text = pattern.sub("*" * len(word), text)
    return text

def clean_strict(text, language):
    """
    Marchează clar cuvintele vulgare detectate (strict).
    """
    for word in VULGAR_WORDS.get(language, []):
        pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
        text = pattern.sub(f"[BLOCKED:{word.upper()}]", text)
    return text