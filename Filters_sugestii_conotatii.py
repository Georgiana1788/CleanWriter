def clean_text(text, lang="română", mode="soft"):
    bad_words = {
        "română": ["pula", "muie", "cur", "dracu"],
        "engleză": ["fuck", "shit", "bitch", "asshole"],
        "germană": ["scheisse", "fick", "arsch"],
        "italiană": ["cazzo", "stronzo", "puttana"]
    }

    sexual_suggestions = {
        "română": ["dă-i la muie", "fă sex", "suge pula", "mănâncă cur"],
        "engleză": ["give head", "suck dick", "eat ass"],
        "germană": ["blase ihn", "arsch lecken"],
        "italiană": ["fai sesso", "pompino"]
    }

    words_to_filter = bad_words.get(lang, []) + sexual_suggestions.get(lang, [])

    for phrase in words_to_filter:
        if phrase in text.lower():
            if mode == "soft":
                text = text.replace(phrase, "*" * len(phrase))
            elif mode == "strict":
                text = text.replace(phrase, f"[CENSORED:{phrase}]")

    return text