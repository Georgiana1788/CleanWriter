# multilang_cleanwriter_interactive.py
from cleanwriter_filter import clean_text

def main():
    print("CleanWriter - Filtru pentru limbaj vulgar și nepotrivit")
    print("Alege limba [ro/en/de/it]: ")
    lang = input(">>> ").strip().lower()
    if lang not in ["ro", "en", "de", "it"]:
        print("Limba aleasă nu este suportată.")
        return

    text = input("Scrie textul pe care vrei să îl verifici: ")

    filtered_text = clean_text(text, lang)
    print("\n--- Rezultat filtrat ---")
    print(filtered_text)

if __name__ == "__main__":
    main()