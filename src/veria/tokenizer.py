import re
import unicodedata


def text_cleaning(text: str) -> list[str]:
    text = unicodedata.normalize("NFKC", text)
    preprocessed = re.split(r"[^\w\s\d]+|[_\s\-]+", text.casefold())
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    return preprocessed
