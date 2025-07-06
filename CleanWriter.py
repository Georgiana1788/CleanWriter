# cleanwriter.py

import argparse
from filters import clean_soft, clean_strict

def main():
    parser = argparse.ArgumentParser(description="CleanWriter CLI - Filtru moral & limbaj")
    parser.add_argument("text", help="Textul de procesat")
    parser.add_argument("-l", "--lang", default="română", choices=["română", "engleză", "germană", "italiană"])
    parser.add_argument("-m", "--mode", default="soft", choices=["soft", "strict"], help="Modul filtrului")

    args = parser.parse_args()

    if args.mode == "soft":
        cleaned = clean_soft(args.text, args.lang)
    else:
        cleaned = clean_strict(args.text, args.lang)

    print("\nRezultat filtrat:")
    print(cleaned)

if __name__ == "__main__":
    main()