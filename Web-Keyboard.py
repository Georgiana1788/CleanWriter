import streamlit as st
from langdetect import detect

FILTERS = {
    "ro": {"sensibile": ["muie", "pula", "cur", "dracu", "rahat"], "alt": "(limbaj decent)"},
    "en": {"sensibile": ["fuck", "shit", "bitch"], "alt": "(be polite)"},
    "de": {"sensibile": ["scheiße", "fick"], "alt": "(höflich bleiben)"},
    "it": {"sensibile": ["cazzo", "merda"], "alt": "(usa parole gentili)"}
}

def clean_text(text, lang):
    sens = FILTERS.get(lang, {}).get("sensibile", [])
    alt = FILTERS.get(lang, {}).get("alt", "***")
    for w in sens:
        text = text.replace(w, alt)
    return text

st.title("📝 Text Cleaner Multilingv")
text = st.text_area("Scrie aici textul tău:")

if text:
    lang = detect(text)
    cleaned = clean_text(text.lower(), lang)
    st.markdown(f"**Limbă detectată:** `{lang}`")
    st.markdown(f"✅ **Text curățat:**\n\n{cleaned}")