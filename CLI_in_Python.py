import argparse
from filters import clean_text

def main():
    parser = argparse.ArgumentParser(description="CleanWriter - moral & language filter")
    parser.add_argument("text", type=str, help="Textul de filtrat")
    parser.add_argument("-l", "--lang", choices=["română", "engleză", "germană", "italiană"], default="română", help="Limba textului")
    parser.add_argument("-m", "--mode", choices=["soft", "strict"], default="soft", help="Modul filtrului")
    args = parser.parse_args()

    filtered = clean_text(args.text, lang=args.lang, mode=args.mode)
    print(f"\n🧹 Text filtrat ({args.lang}, {args.mode}):\n{filtered}")

if __name__ == "__main__":
    main()