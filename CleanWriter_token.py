import spacy

# Load SpaCy small English model
nlp = spacy.load("en_core_web_sm")

# List of soft moral filters
soft_bad_words = ["damn", "hell", "crap"]
# List of strict offensive words
strict_bad_words = ["fuck", "shit", "bitch", "asshole", "cunt"]

def clean_text(text):
    doc = nlp(text)
    cleaned_tokens = []
    for token in doc:
        token_lower = token.text.lower()
        if token_lower in strict_bad_words:
            cleaned_tokens.append("[CENSORED]")
        elif token_lower in soft_bad_words:
            cleaned_tokens.append("[SOFT-CLEANED]")
        else:
            cleaned_tokens.append(token.text)
    return " ".join(cleaned_tokens)

if __name__ == "__main__":
    print("Welcome to CleanWriter CLI!")
    text_input = input("Enter your text: ")
    result = clean_text(text_input)
    print("Filtered text:\n", result)