from bs4 import BeautifulSoup

def clean_text(title: str, description: str) -> str:
    combined = f"{title} {description}"
    cleaned = BeautifulSoup(combined, "html.parser").get_text(separator=" ")
    return " ".join(cleaned.split())