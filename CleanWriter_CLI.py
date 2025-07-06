import argparse
from cleanwriter_filter import clean_text

parser = argparse.ArgumentParser(description="CleanWriter CLI - filtrează și curăță textul.")
parser.add_argument("text", type=str, help="Textul de filtrat")
parser.add_argument("--lang", type=str, choices=["en", "ro", "de", "it"], default="en", help="Limba textului")
args = parser.parse_args()

cleaned = clean_text(args.text, lang=args.lang)
print(f"\n✅ Text filtrat:\n{cleaned}")