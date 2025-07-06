import streamlit as st
from cleanwriter_filter import clean_text

st.title("CleanWriter Web")
st.write("Filtrează textul și elimină limbajul vulgar.")

text = st.text_area("Introdu textul aici:")
lang = st.selectbox("Alege limba", ["en", "ro", "de", "it"])

if st.button("Filtrează"):
    cleaned = clean_text(text, lang=lang)
    st.success(f"✅ Text filtrat:\n{cleaned}")