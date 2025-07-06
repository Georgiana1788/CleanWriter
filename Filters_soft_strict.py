def clean_text(text, lang="română", mode="soft"):
    bad_words = {
        "română": ["pula", "muie", "cur", "dracu"],
        "engleză": ["fuck", "shit", "bitch", "asshole"],
        "germană": ["scheisse", "fick", "arsch"],
        "italiană": ["cazzo", "stronzo", "puttana"]
    }

    words_to_filter = bad_words.get(lang, [])

    for word in words_to_filter:
        if mode == "soft":
            text = text.replace(word, "*" * len(word))
        elif mode == "strict":
            text = text.replace(word, f"[CENSORED:{word}]")

    return text